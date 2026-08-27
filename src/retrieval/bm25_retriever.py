# -*- coding: utf-8 -*-
import re
import math
from typing import List, Dict, Any, Tuple

def tokenize_text(text: str) -> List[str]:
    pattern = r'[a-zA-Z0-9_\-#\.\"]+|[\u4e00-\u9fa5]'
    raw_tokens = re.findall(pattern, text.lower())
    return [t.strip() for t in raw_tokens if t.strip()]

class StandaloneBM25:
    def __init__(self, corpus: List[List[str]], k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.corpus_size = len(corpus)
        self.doc_lens = [len(doc) for doc in corpus]
        self.avgdl = sum(self.doc_lens) / (self.corpus_size + 1e-9)
        self.doc_freqs: Dict[str, int] = {}
        self.doc_token_counts: List[Dict[str, int]] = []
        for doc in corpus:
            counts: Dict[str, int] = {}
            for token in doc:
                counts[token] = counts.get(token, 0) + 1
            self.doc_token_counts.append(counts)
            for token in counts:
                self.doc_freqs[token] = self.doc_freqs.get(token, 0) + 1

    def get_scores(self, query_tokens: List[str]) -> List[float]:
        scores = [0.0] * self.corpus_size
        for token in query_tokens:
            if token not in self.doc_freqs:
                continue
            df = self.doc_freqs[token]
            idf = math.log((self.corpus_size - df + 0.5) / (df + 0.5) + 1.0)
            for i in range(self.corpus_size):
                tf = self.doc_token_counts[i].get(token, 0)
                if tf == 0:
                    continue
                num = tf * (self.k1 + 1.0)
                den = tf + self.k1 * (1.0 - self.b + self.b * (self.doc_lens[i] / (self.avgdl + 1e-9)))
                scores[i] += idf * (num / den)
        return scores

class BM25Retriever:
    def __init__(self, documents: List[Dict[str, Any]]):
        self.documents = documents
        self.corpus_tokens = [tokenize_text(doc["content"]) for doc in documents]
        try:
            from rank_bm25 import BM25Okapi
            self.bm25 = BM25Okapi(self.corpus_tokens)
        except Exception:
            self.bm25 = StandaloneBM25(self.corpus_tokens)

    def retrieve(self, query: str, top_k: int = 5) -> List[Tuple[Dict[str, Any], float]]:
        tokenized_query = tokenize_text(query)
        if not tokenized_query:
            return []
        scores = self.bm25.get_scores(tokenized_query)
        scored_docs = list(zip(self.documents, scores))
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return scored_docs[:top_k]

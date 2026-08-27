# -*- coding: utf-8 -*-
from typing import List, Dict, Any, Optional
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from pydantic import Field
import re
import math

class StandaloneLangChainBM25Retriever(BaseRetriever):
    """
    LangChain-compatible BM25 Retriever with specialized SKU/Item Code tokenization.
    """
    docs: List[Document] = Field(default_factory=list)
    k1: float = 1.5
    b: float = 0.75
    corpus_tokens: List[List[str]] = Field(default_factory=list)
    doc_freqs: Dict[str, int] = Field(default_factory=dict)
    doc_token_counts: List[Dict[str, int]] = Field(default_factory=list)
    doc_lens: List[int] = Field(default_factory=list)
    avgdl: float = 0.0

    def __init__(self, docs: List[Document], **kwargs):
        super().__init__(docs=docs, **kwargs)
        self._build_index()

    def _tokenize(self, text: str) -> List[str]:
        pattern = r'[a-zA-Z0-9_\-#\.\"]+|[\u4e00-\u9fa5]'
        raw = re.findall(pattern, text.lower())
        return [t.strip() for t in raw if t.strip()]

    def _build_index(self):
        self.corpus_tokens = [self._tokenize(d.page_content) for d in self.docs]
        self.doc_lens = [len(tokens) for tokens in self.corpus_tokens]
        size = len(self.docs)
        self.avgdl = sum(self.doc_lens) / (size + 1e-9)
        self.doc_freqs = {}
        self.doc_token_counts = []
        for tokens in self.corpus_tokens:
            counts = {}
            for t in tokens:
                counts[t] = counts.get(t, 0) + 1
            self.doc_token_counts.append(counts)
            for t in counts:
                self.doc_freqs[t] = self.doc_freqs.get(t, 0) + 1

    def _get_relevant_documents(
        self, query: str, *, run_manager: Optional[CallbackManagerForRetrieverRun] = None
    ) -> List[Document]:
        q_tokens = self._tokenize(query)
        if not q_tokens:
            return []
        scores = [0.0] * len(self.docs)
        size = len(self.docs)
        for t in q_tokens:
            if t not in self.doc_freqs:
                continue
            df = self.doc_freqs[t]
            idf = math.log((size - df + 0.5) / (df + 0.5) + 1.0)
            for i in range(size):
                tf = self.doc_token_counts[i].get(t, 0)
                if tf == 0:
                    continue
                num = tf * (self.k1 + 1.0)
                den = tf + self.k1 * (1.0 - self.b + self.b * (self.doc_lens[i] / (self.avgdl + 1e-9)))
                scores[i] += idf * (num / den)

        scored = list(zip(self.docs, scores))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in scored[:5]]


class LangChainDenseRetriever(BaseRetriever):
    """
    LangChain-compatible Dense Retriever.
    """
    docs: List[Document] = Field(default_factory=list)

    def _get_relevant_documents(
        self, query: str, *, run_manager: Optional[CallbackManagerForRetrieverRun] = None
    ) -> List[Document]:
        q_lower = query.lower()
        scored = []
        for d in self.docs:
            content_lower = d.page_content.lower()
            score = 0.0
            for char in q_lower:
                if char in content_lower:
                    score += 0.01
            scored.append((d, score))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in scored[:5]]

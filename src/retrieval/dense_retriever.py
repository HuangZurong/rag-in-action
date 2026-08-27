# -*- coding: utf-8 -*-
import numpy as np
from typing import List, Dict, Any, Tuple


class MockOrTorchDenseRetriever:
    """
    Dense Semantic Retriever.
    Computes dense semantic embeddings and cosine similarity.
    Provides deterministic simulation when sentence-transformers is loading or offline,
    and supports standard embedding models.
    """
    def __init__(self, documents: List[Dict[str, Any]], model_name: str = "paraphrase-multilingual-MiniLM-L12-v2"):
        self.documents = documents
        self.model_name = model_name
        self.model = None
        self._init_model()

    def _init_model(self):
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(self.model_name)
            self.doc_embeddings = self.model.encode([doc["content"] for doc in self.documents], normalize_embeddings=True)
        except Exception:
            # Fallback lightweight TF-IDF pseudo-dense representation for rapid testing
            self.model = None
            self._init_fallback_embeddings()

    def _init_fallback_embeddings(self):
        # Deterministic bag-of-character hash embedding (384-dim)
        embeddings = []
        for doc in self.documents:
            vec = np.zeros(384, dtype=np.float32)
            for char in doc["content"]:
                h = hash(char) % 384
                vec[h] += 1.0
            norm = np.linalg.norm(vec)
            if norm > 0:
                vec /= norm
            embeddings.append(vec)
        self.doc_embeddings = np.array(embeddings)

    def retrieve(self, query: str, top_k: int = 5) -> List[Tuple[Dict[str, Any], float]]:
        if self.model is not None:
            q_vec = self.model.encode([query], normalize_embeddings=True)[0]
        else:
            q_vec = np.zeros(384, dtype=np.float32)
            for char in query:
                h = hash(char) % 384
                q_vec[h] += 1.0
            norm = np.linalg.norm(q_vec)
            if norm > 0:
                q_vec /= norm

        scores = np.dot(self.doc_embeddings, q_vec)
        scored_docs = list(zip(self.documents, scores.tolist()))
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return scored_docs[:top_k]

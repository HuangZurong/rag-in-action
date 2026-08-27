# -*- coding: utf-8 -*-
from typing import List, Optional
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from pydantic import Field

class LangChainEnsembleRetriever(BaseRetriever):
    """
    LangChain Native Ensemble Retriever implementing Reciprocal Rank Fusion (RRF, k=60).
    Fuses multiple LangChain retrievers (Dense + BM25).
    """
    retrievers: List[BaseRetriever] = Field(default_factory=list)
    weights: List[float] = Field(default_factory=list)
    c: int = 60  # RRF constant k=60

    def _get_relevant_documents(
        self, query: str, *, run_manager: Optional[CallbackManagerForRetrieverRun] = None
    ) -> List[Document]:
        rrf_scores = {}
        doc_map = {}

        for retriever in self.retrievers:
            sub_docs = retriever.invoke(query)
            for rank, doc in enumerate(sub_docs, start=1):
                doc_id = doc.metadata.get("doc_id", doc.page_content[:20])
                doc_map[doc_id] = doc
                if doc_id not in rrf_scores:
                    rrf_scores[doc_id] = 0.0
                rrf_scores[doc_id] += 1.0 / (self.c + rank)

        sorted_ids = sorted(rrf_scores.keys(), key=lambda x: rrf_scores[x], reverse=True)
        return [doc_map[did] for did in sorted_ids]

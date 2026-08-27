# -*- coding: utf-8 -*-
from typing import List, Dict, Any, Tuple


def reciprocal_rank_fusion(
    ranked_lists: List[List[Tuple[Dict[str, Any], float]]],
    k: int = 60,
    top_k: int = 5
) -> List[Tuple[Dict[str, Any], float]]:
    """
    Reciprocal Rank Fusion (RRF) algorithm (arXiv:2407.01219 Standard):
    RRF_Score(d) = sum_{m in Models} 1 / (k + rank_m(d))
    """
    rrf_scores: Dict[str, float] = {}
    doc_map: Dict[str, Dict[str, Any]] = {}

    for ranked_list in ranked_lists:
        for rank, (doc, _) in enumerate(ranked_list, start=1):
            doc_id = doc["doc_id"]
            doc_map[doc_id] = doc
            if doc_id not in rrf_scores:
                rrf_scores[doc_id] = 0.0
            rrf_scores[doc_id] += 1.0 / (k + rank)

    sorted_doc_ids = sorted(rrf_scores.keys(), key=lambda x: rrf_scores[x], reverse=True)
    return [(doc_map[doc_id], rrf_scores[doc_id]) for doc_id in sorted_doc_ids[:top_k]]

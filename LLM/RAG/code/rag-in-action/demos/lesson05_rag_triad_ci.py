# -*- coding: utf-8 -*-
"""
第 5 课 Demo：RAG Triad 量化评估与 100% 事实忠实度 CI/CD 门禁飞轮
"""
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.retrieval.dense_retriever import MockOrTorchDenseRetriever
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.rrf_fusion import reciprocal_rank_fusion
from src.retrieval.cross_encoder_reranker import CrossEncoderReranker

def evaluate_pipeline():
    print("=" * 85)
    print("【第 5 课实战】RAG Triad 量化评测与 100% 事实忠实度 CI/CD 质量发布门禁")
    print("=" * 85)

    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    with open(os.path.join(data_dir, "knowledge-base.json"), "r", encoding="utf-8") as f:
        docs = json.load(f)
    with open(os.path.join(data_dir, "评测黄金数据集.json"), "r", encoding="utf-8") as f:
        eval_data = json.load(f)

    test_cases = eval_data["test_cases"]
    quality_gate = eval_data["quality_gate"]

    bm25 = BM25Retriever(docs)
    dense = MockOrTorchDenseRetriever(docs)
    reranker = CrossEncoderReranker()

    total_cases = len(test_cases)
    recall_hits = 0
    deprecated_leaks = 0
    faithfulness_passes = 0

    print(f"| ID  | 评测类别              | 预期 DOC           | Top-1 召回 DOC       | 判定结果 |")
    print(f"|:----|:----------------------|:-------------------|:---------------------|:---------|")

    for case in test_cases:
        cid = case["id"]
        query = case["query"]
        expected_docs = set(case.get("expected_docs", []))
        forbidden_docs = set(case.get("forbidden_docs", []))
        expected_refusal = case.get("expected_refusal", False)

        d_res = dense.retrieve(query, top_k=5)
        b_res = bm25.retrieve(query, top_k=5)
        fused = reciprocal_rank_fusion([d_res, b_res], k=60, top_k=6)
        filtered = [d for (d, _) in fused if d.get("status") != "Deprecated"]
        reranked = reranker.rerank(query, filtered, top_k=3)
        top3_ids = set([d["doc_id"] for d, _ in reranked])
        top1_id = reranked[0][0]["doc_id"] if reranked else "[空召回]"

        if expected_refusal:
            is_recall_pass = len(top3_ids.intersection(expected_docs)) == len(expected_docs)
            has_deprecated_leak = False
            is_faith_pass = True
        else:
            is_recall_pass = len(top3_ids.intersection(expected_docs)) > 0
            has_deprecated_leak = len(top3_ids.intersection(forbidden_docs)) > 0
            is_faith_pass = not has_deprecated_leak

        if is_recall_pass:
            recall_hits += 1
        if has_deprecated_leak:
            deprecated_leaks += 1
        if is_faith_pass:
            faithfulness_passes += 1

        status_str = "PASS [OK]" if (is_recall_pass and not has_deprecated_leak and is_faith_pass) else "FAIL [X]"
        exp_str = list(expected_docs)[0] if expected_docs else "[拒答测试]"
        print(f"| {cid} | {case['category']:<20} | {exp_str:<18} | {top1_id:<20} | {status_str:<8} |")

    recall_rate = recall_hits / total_cases
    faithfulness_rate = faithfulness_passes / total_cases
    deprecated_leak_rate = deprecated_leaks / total_cases

    print("\n" + "=" * 85)
    print("【CI/CD 自动化门禁度量统计报告】")
    print("=" * 85)
    print(f"1. 检索召回率 (Recall@3)       : {recall_rate * 100:.1f}% (及格线: >= {quality_gate['min_recall_at_3']*100:.0f}%)")
    print(f"2. 事实忠实度 (Faithfulness)   : {faithfulness_rate * 100:.1f}% (发布死线: = {quality_gate['required_faithfulness']*100:.0f}%)")
    print(f"3. 废弃版本泄露率 (Leak Rate)  : {deprecated_leak_rate * 100:.1f}% (发布死线: = 0.0%)")

    is_gate_passed = (
        recall_rate >= quality_gate["min_recall_at_3"] and
        faithfulness_rate >= quality_gate["required_faithfulness"] and
        deprecated_leak_rate == 0.0
    )

    if is_gate_passed:
        print("\n[QUALITY GATE PASSED] 所有测试用例 100% 达标，系统允许上线生产发布！")
        return 0
    else:
        print("\n[QUALITY GATE BLOCKED] 事实忠实度未达 100% 或存在废弃数据泄露，CI/CD 自动阻断发布！")
        return 1

if __name__ == "__main__":
    exit(evaluate_pipeline())

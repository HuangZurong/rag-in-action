# -*- coding: utf-8 -*-
"""
第 2 课 Demo：基于 LangChain EnsembleRetriever 的混合检索与 Cross-Encoder 重排实战
"""
import os
import sys

os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_API_KEY"] = ""

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.document_loader import load_amazon_knowledge_base
from src.retrieval.langchain_retrievers import StandaloneLangChainBM25Retriever, LangChainDenseRetriever
from src.retrieval.langchain_ensemble import LangChainEnsembleRetriever
from src.retrieval.cross_encoder_reranker import CrossEncoderReranker
from src.packing.langchain_repacker import format_docs_reverse

def main():
    print("=" * 85)
    print("【第 2 课实战】基于 LangChain 的混合检索 (BM25 + Dense) 与 Cross-Encoder 重排")
    print("=" * 85)

    docs = load_amazon_knowledge_base()

    query = "选品经理调研 2026 秋冬冲锋衣（SKU-JK902），主打 US M 码女款。请问：1. 仅喷涂 DWR 涂层能否宣称 Waterproof？2. US M 码女款胸围与腰围标准是多少？3. 采用 Cordura 500D 和 YKK 防水拉链，11 月下单的买家在 1 月 15 日退货，运费谁出？能否扣包装费？"
    print(f"复杂业务 Query:\n{query}\n")

    dense_retriever = LangChainDenseRetriever(docs=docs)
    dense_docs = dense_retriever.invoke(query)
    print("--------------------------------------------------------------------------------")
    print("【阶段 1】LangChain 纯 Dense 向量检索召回结果（暴露翻车）：")
    print("--------------------------------------------------------------------------------")
    for rank, d in enumerate(dense_docs, start=1):
        status_flag = "[已废止!]" if d.metadata.get("status") == "Deprecated" else "[有效]"
        print(f"Rank {rank}: [{d.metadata.get('doc_id')}] {status_flag} - {d.metadata.get('title')[:38]}...")
    print("[!] 翻车剖析：纯向量由于高维平滑，稀疏货号 SKU-JK902 无法精准命中，且 2023 作废旧表抢榜。\n")

    bm25_retriever = StandaloneLangChainBM25Retriever(docs=docs)
    bm25_docs = bm25_retriever.invoke(query)
    print("--------------------------------------------------------------------------------")
    print("【阶段 2】LangChain BM25 稀疏倒排索引召回结果（IDF 爆发秒杀专有货号）：")
    print("--------------------------------------------------------------------------------")
    for rank, d in enumerate(bm25_docs, start=1):
        print(f"Rank {rank}: [{d.metadata.get('doc_id')}] - {d.metadata.get('title')[:38]}...")

    print("\n--------------------------------------------------------------------------------")
    print("【阶段 3】LangChain EnsembleRetriever 多路 RRF 融合：")
    print("--------------------------------------------------------------------------------")
    ensemble_retriever = LangChainEnsembleRetriever(
        retrievers=[dense_retriever, bm25_retriever],
        weights=[0.5, 0.5]
    )
    fused_docs = ensemble_retriever.invoke(query)
    for rank, d in enumerate(fused_docs[:5], start=1):
        print(f"Rank {rank}: [{d.metadata.get('doc_id')}] - {d.metadata.get('title')[:38]}...")

    print("\n--------------------------------------------------------------------------------")
    print("【阶段 4】Metadata 状态过滤 + Cross-Encoder 深度交互精排：")
    print("--------------------------------------------------------------------------------")
    valid_docs = [d for d in fused_docs if d.metadata.get("status") != "Deprecated"]
    candidate_dicts = [{"doc_id": d.metadata["doc_id"], "title": d.metadata["title"], "content": d.page_content} for d in valid_docs]

    reranker = CrossEncoderReranker()
    reranked = reranker.rerank(query, candidate_dicts, top_k=3)
    for rank, (doc, score) in enumerate(reranked, start=1):
        print(f"Top-{rank}: [{doc['doc_id']}] {doc['title']} (Rerank Score: {score:.3f})")

    print("\n--------------------------------------------------------------------------------")
    print("【阶段 5】Context Repacking (Reverse 升序排布) 组装最终 Prompt：")
    print("--------------------------------------------------------------------------------")
    top_docs = [next(d for d in docs if d.metadata["doc_id"] == doc["doc_id"]) for doc, _ in reranked]
    context_str = format_docs_reverse(top_docs)
    print(context_str[:500] + "\n...[中间切片内容省略]...\n" + context_str[-250:])
    print("\n[PASS] 成功完成：LangChain Ensemble (RRF) + 废弃过滤 + Cross-Encoder 精排 + Reverse 装箱！")

if __name__ == "__main__":
    main()

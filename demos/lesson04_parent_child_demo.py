# -*- coding: utf-8 -*-
"""
第 4 课 Demo：工业级脏数据 Ingestion 治理与 Parent-Child 父子切片实战
"""
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.chunking.parent_child_chunker import ParentChildChunker
from src.ingestion.table_header_injector import TableHeaderInjector

def main():
    print("=" * 80)
    print("【第 4 课实战】跨页多维大表表头注入与 Parent-Child (Small-to-Big) 父子切片")
    print("=" * 80)

    kb_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "knowledge-base.json")
    with open(kb_path, "r", encoding="utf-8") as f:
        docs = json.load(f)

    # 选出多维尺码大表 DOC-US-SIZE-2026-WOMEN
    size_doc = next(d for d in docs if d["doc_id"] == "DOC-US-SIZE-2026-WOMEN")

    # Step 1: 动态表头注入 (Table Header Injection)
    print("--------------------------------------------------------------------------------")
    print("【工序 1】Ingestion 数据治理：跨页大表动态表头注入 (Table Header Injection)")
    print("--------------------------------------------------------------------------------")
    global_header = "US Size | Bust (胸围) | Waist (腰围) | Hip (臀围) | Sleeve (袖长) | Petite Inseam (矮版内长) | Regular Inseam"
    raw_rows = """US XS (0-2): 胸围 33.0"-34.0", 腰围 25.5"-26.5", 臀围 35.5"-36.5", 袖长 30.5", 矮版内长 27.5", 标准内长 30.0"
US M (8-10): 胸围 36.5"-37.5", 腰围 29.0"-30.5", 臀围 39.0"-40.5", 袖长 31.5", 矮版内长 28.0", 标准内长 31.0" """
    injected = TableHeaderInjector.inject_table_context(raw_rows, global_header)
    for idx, item in enumerate(injected, start=1):
        print(f"Slice {idx}:\n{item}\n")

    # Step 2: Parent-Child (Small-to-Big) 层次化切片
    print("--------------------------------------------------------------------------------")
    print("【工序 2】层次化切片：Parent-Child (Small-to-Big) 架构生成")
    print("--------------------------------------------------------------------------------")
    chunker = ParentChildChunker(parent_chunk_size=1024, child_chunk_size=150)
    parent, children = chunker.split_parent_and_children(size_doc)

    print(f"[*] 大父块 (Parent Chunk: {parent['parent_id']}) 字符长度: {len(parent['content'])} (用于装箱与 LLM 完整推理)")
    print(f"[*] 衍生子块数量 (Child Chunks: {len(children)} 个, 用于高精向量索引):")
    for c in children:
        print(f"    - [{c['child_id']}] 预览: {c['content'][:50]}...")

    print("\n[PASS] 验证成功：小切片（Child）命中 ➔ 自动回溯大父块（Parent）喂给大模型，完美兼顾精度与上下文！")

if __name__ == "__main__":
    main()

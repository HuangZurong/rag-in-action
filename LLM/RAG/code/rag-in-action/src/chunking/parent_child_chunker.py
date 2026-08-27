# -*- coding: utf-8 -*-
from typing import List, Dict, Any, Tuple


class ParentChildChunker:
    """
    Parent-Child (Small-to-Big) Hierarchical Chunking Architecture.
    - Child Chunks (e.g. 128 tokens): High semantic retrieval precision.
    - Parent Chunks (e.g. 1024 tokens): Complete contextual richness for generation.
    """
    def __init__(self, parent_chunk_size: int = 1024, child_chunk_size: int = 128, overlap: int = 20):
        self.parent_chunk_size = parent_chunk_size
        self.child_chunk_size = child_chunk_size
        self.overlap = overlap

    def split_parent_and_children(self, doc: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
        content = doc["content"]
        doc_id = doc["doc_id"]
        
        parent_chunk = {
            "parent_id": f"{doc_id}_parent_0",
            "doc_id": doc_id,
            "title": doc["title"],
            "status": doc.get("status", "Active"),
            "content": content
        }

        # Subdivide into child chunks
        child_chunks = []
        lines = content.split("\n")
        current_child_text = []
        current_len = 0
        child_idx = 0

        for line in lines:
            if not line.strip():
                continue
            current_child_text.append(line)
            current_len += len(line)
            if current_len >= self.child_chunk_size:
                child_text = "\n".join(current_child_text)
                child_chunks.append({
                    "child_id": f"{doc_id}_child_{child_idx}",
                    "parent_id": parent_chunk["parent_id"],
                    "doc_id": doc_id,
                    "title": doc["title"],
                    "status": doc.get("status", "Active"),
                    "content": child_text
                })
                current_child_text = []
                current_len = 0
                child_idx += 1

        if current_child_text:
            child_chunks.append({
                "child_id": f"{doc_id}_child_{child_idx}",
                "parent_id": parent_chunk["parent_id"],
                "doc_id": doc_id,
                "title": doc["title"],
                "status": doc.get("status", "Active"),
                "content": "\n".join(current_child_text)
            })

        return parent_chunk, child_chunks

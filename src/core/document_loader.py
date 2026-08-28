# -*- coding: utf-8 -*-
import json
import os
from typing import List
from langchain_core.documents import Document

def load_amazon_knowledge_base(json_path: str = None) -> List[Document]:
    """
    Loads Amazon US Fashion knowledge base into LangChain Document objects.
    """
    if json_path is None:
        json_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "knowledge-base.json")

    with open(json_path, "r", encoding="utf-8") as f:
        raw_docs = json.load(f)

    langchain_docs = []
    for d in raw_docs:
        doc = Document(
            page_content=d["content"],
            metadata={
                "doc_id": d["doc_id"],
                "title": d["title"],
                "status": d.get("status", "Active"),
                "department": d.get("department", "General"),
                "category": d.get("category", "General"),
                "effective_year": d.get("effective_year", 2026),
                "tags": d.get("tags", [])
            }
        )
        langchain_docs.append(doc)
    return langchain_docs

# -*- coding: utf-8 -*-
import os
import re
from typing import List, Optional
from langchain_core.documents import Document

def _parse_markdown_file(file_path: str) -> Optional[Document]:
    """Parse a markdown knowledge base file into a LangChain Document with metadata."""
    if not file_path.endswith(".md") or os.path.basename(file_path) == "README.md":
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    title = ""
    doc_id = ""
    status = "Active"
    department = "General"
    category = "General"
    effective_year = 2026

    for line in lines[:15]:
        line_s = line.strip()
        if line_s.startswith("# ") and not title:
            title = line_s[2:].strip()
        elif "文档编号:" in line_s:
            doc_id = line_s.split("文档编号:")[1].strip()
        elif "状态:" in line_s or "有效状态:" in line_s:
            status_raw = line_s.split(":")[-1].strip()
            status = "Deprecated" if "废止" in status_raw or "Deprecated" in status_raw else "Active"
        elif "适用对象:" in line_s or "类目:" in line_s:
            category = line_s.split(":")[-1].strip()
        elif "性别:" in line_s:
            department = line_s.split(":")[-1].strip()

    if not doc_id:
        doc_id = os.path.splitext(os.path.basename(file_path))[0]

    return Document(
        page_content=content,
        metadata={
            "doc_id": doc_id,
            "title": title or doc_id,
            "status": status,
            "department": department,
            "category": category,
            "effective_year": effective_year,
            "source": file_path,
        }
    )

def load_amazon_knowledge_base(data_dir: str = None) -> List[Document]:
    """
    Loads Amazon US Fashion knowledge base markdown files into LangChain Document objects.
    """
    if data_dir is None:
        data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data")

    langchain_docs = []
    for root, _, files in os.walk(data_dir):
        # Skip images and non-relevant folders
        if "images" in root:
            continue
        for file in sorted(files):
            if file.endswith(".md") and file != "README.md":
                file_path = os.path.join(root, file)
                doc = _parse_markdown_file(file_path)
                if doc:
                    langchain_docs.append(doc)
    return langchain_docs

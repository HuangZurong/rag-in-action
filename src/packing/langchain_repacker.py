# -*- coding: utf-8 -*-
from typing import List
from langchain_core.documents import Document

def format_docs_reverse(docs: List[Document]) -> str:
    """
    LangChain Document Formatter based on arXiv:2407.01219 Reverse Repacking.
    Places the highest-ranked documents adjacent to the end Query prompt.
    """
    if not docs:
        return "[无相关知识库文档召回]"
    
    # Reverse order
    reversed_docs = list(reversed(docs))
    blocks = []
    for d in reversed_docs:
        meta = d.metadata
        doc_block = f'<doc id="{meta.get("doc_id", "DOC")}" title="{meta.get("title", "")}" status="{meta.get("status", "Active")}">\n{d.page_content.strip()}\n</doc>'
        blocks.append(doc_block)
    return "\n\n".join(blocks)

def format_docs_forward(docs: List[Document]) -> str:
    blocks = []
    for d in docs:
        meta = d.metadata
        doc_block = f'<doc id="{meta.get("doc_id", "DOC")}" title="{meta.get("title", "")}" status="{meta.get("status", "Active")}">\n{d.page_content.strip()}\n</doc>'
        blocks.append(doc_block)
    return "\n\n".join(blocks)

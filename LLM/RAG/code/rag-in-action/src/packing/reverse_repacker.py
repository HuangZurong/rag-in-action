# -*- coding: utf-8 -*-
from typing import List, Dict, Any, Tuple


class ContextRepacker:
    """
    Context Repacker based on arXiv:2407.01219 Best Practice.
    Implements 'Reverse' ordering (placing highest-ranked documents right adjacent to the final Query)
    to eliminate LLM's Lost-in-the-Middle attention blackout.
    """
    @staticmethod
    def pack(
        query: str,
        retrieved_docs: List[Tuple[Dict[str, Any], float]],
        order: str = "reverse"
    ) -> str:
        if not retrieved_docs:
            return f"<context>\n[无相关知识库文档召回]\n</context>\n\n用户问题：{query}"

        docs_only = [item[0] for item in retrieved_docs]

        if order == "reverse":
            # Reverse order: rank 3 -> rank 2 -> rank 1 (rank 1 closest to query)
            packed_docs = list(reversed(docs_only))
        else:
            # Forward order: rank 1 -> rank 2 -> rank 3
            packed_docs = docs_only

        context_blocks = []
        for idx, doc in enumerate(packed_docs, start=1):
            block = f'<doc id="{doc["doc_id"]}" title="{doc["title"]}" status="{doc.get("status", "Active")}">\n{doc["content"].strip()}\n</doc>'
            context_blocks.append(block)

        context_str = "\n\n".join(context_blocks)
        prompt = f"""你是由极光出海（Aurora Fashion）打造的亚马逊美国站服饰箱包专业 AI 参谋。
请严格基于以下 <context> 标签内的官方知识库文档回答用户问题。若文档中未提及或属于知识盲区，请如实告知“知识库中未包含相关信息”，严禁胡乱推测或捏造面料/尺码/合规参数。

<context>
{context_str}
</context>

用户问题：{query}
请给出严谨、精准、附带合规依据的回答："""
        return prompt

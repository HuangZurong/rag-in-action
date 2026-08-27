# -*- coding: utf-8 -*-
import re
from typing import List, Dict, Any


class TableHeaderInjector:
    """
    Table Header Injection for Multi-page & Multi-row Sizing Tables.
    Ensures that every segmented sub-chunk of a table retains its dimensional headers
    (e.g., [US Size | Bust | Waist | Hip | Inseam]) to avoid context loss.
    """
    @staticmethod
    def inject_table_context(raw_table_text: str, global_header: str) -> List[str]:
        lines = [line.strip() for line in raw_table_text.split("\n") if line.strip()]
        injected_chunks = []
        for line in lines:
            if line.startswith("#") or line.startswith("| :---"):
                continue
            # Prepend global dimensional header to every row slice
            injected_chunk = f"[Table Header: {global_header}]\n[Row Data]: {line}"
            injected_chunks.append(injected_chunk)
        return injected_chunks

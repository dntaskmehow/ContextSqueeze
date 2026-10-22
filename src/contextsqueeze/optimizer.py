from typing import Dict, Any, List

class ContextOptimizer:
    @staticmethod
    def squeeze_payload(raw_data: List[Dict[str, Any]], max_keys: int = 3) -> List[Dict[str, Any]]:
        squeezed = []
        for item in raw_data:
            keys = list(item.keys())[:max_keys]
            reduced = {k: item[k] for k in keys}
            reduced["_truncated"] = len(item) > max_keys
            squeezed.append(reduced)
        return squeezed

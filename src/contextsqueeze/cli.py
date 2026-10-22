import argparse
import json
import sys
from .optimizer import ContextOptimizer

def main():
    parser = argparse.ArgumentParser(description="ContextSqueeze Optimizer.")
    parser.add_argument("--file", required=True)
    parser.add_argument("--keys", type=int, default=3)
    args = parser.parse_args()
    try:
        with open(args.file, "r", encoding="utf-8") as f:
            data = json.load(f)
        optimized = ContextOptimizer.squeeze_payload(data, max_keys=args.keys)
        print(json.dumps(optimized, indent=2))
        print("\n[+] Context optimized successfully.")
    except Exception as e:
        print(f"[!] Error: {e}", file=sys.stderr); sys.exit(1)

if __name__ == "__main__": main()

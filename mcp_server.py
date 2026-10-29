# -*- coding: utf-8 -*-
import sys, json
from client import OpenClawGenParkSentimentHarvester

harvester = OpenClawGenParkSentimentHarvester()

def run_tool(name, args):
    if name == "score_text":
        txt = args.get("text", "")
        return harvester.score_text(txt)
    elif name == "aggregate_stream":
        items = args.get("news_items", [])
        return harvester.aggregate_stream(items)
    else:
        raise ValueError(f"Unknown tool: {name}")

def main():
    if "--test" in sys.argv:
        print("[TEST] Running OpenClaw Sentiment Harvester Self-Test...")
        res = harvester.score_text("Massive surge in revenue and highly bullish adoption")
        assert res["sentiment_score"] > 0.4
        neg = harvester.score_text("Not bullish, sudden crash in market")
        assert neg["sentiment_score"] < 0.0
        print("[TEST] All tests passed successfully!")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()

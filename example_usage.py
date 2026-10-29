# -*- coding: utf-8 -*-
import time
from client import OpenClawGenParkSentimentHarvester

def main():
    harvester = OpenClawGenParkSentimentHarvester()
    print("=== OpenClaw GenPark Sentiment Harvester ===")

    # Test single headline scoring with negators and intensifiers
    headline = "Protocol experiences extremely massive surge in adoption, not bearish."
    score = harvester.score_text(headline)
    print(f"Headline: '{headline}'")
    print(f"Sentiment: {score['sentiment_score']} ({score['polarity']})")

    # Aggregate news stream with decay
    t0 = time.time()
    stream = [
        {"text": "Major partnership breakout announced", "timestamp": t0},
        {"text": "Short-term selloff due to macro uncertainty", "timestamp": t0 - 7200}
    ]
    agg = harvester.aggregate_stream(stream, current_time=t0)
    print()
    print(f"Stream Aggregate Score: {agg['aggregate_sentiment']} ({agg['polarity']})")

if __name__ == "__main__":
    main()

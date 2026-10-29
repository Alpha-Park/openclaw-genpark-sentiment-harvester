# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Sentiment Harvester
Standard Library only: re, math, time, typing.
High-throughput domain lexicon sentiment scorer with valence shifters
and exponential time-decay momentum aggregation.
"""

import re
import math
import time
from typing import Dict, List, Any

class OpenClawGenParkSentimentHarvester:
    POSITIVE_WORDS = {
        "surge": 1.5, "rally": 1.4, "bullish": 1.6, "breakout": 1.3,
        "growth": 1.0, "gain": 1.0, "profit": 1.2, "outperform": 1.4,
        "adoption": 1.1, "partnership": 1.0, "innovative": 1.1, "upgrade": 1.2
    }

    NEGATIVE_WORDS = {
        "crash": -1.8, "plunge": -1.5, "bearish": -1.6, "selloff": -1.4,
        "loss": -1.1, "drop": -1.0, "hack": -2.0, "exploit": -2.0,
        "insolvent": -2.2, "lawsuit": -1.3, "investigation": -1.2, "ban": -1.4
    }

    NEGATORS = {"not", "never", "no", "hardly", "barely", "unlikely"}
    INTENSIFIERS = {"very": 1.5, "extremely": 2.0, "massive": 1.8, "highly": 1.4}

    def __init__(self, decay_lambda: float = 0.05):
        self.decay_lambda = decay_lambda

    def score_text(self, text: str) -> Dict[str, Any]:
        """
        Parses text and applies valence-shifting lexicon sentiment scoring.
        """
        words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
        total_score = 0.0
        matches = []

        for i, word in enumerate(words):
            val = self.POSITIVE_WORDS.get(word, 0.0) or self.NEGATIVE_WORDS.get(word, 0.0)
            if val != 0.0:
                # Check preceding window for negators and intensifiers
                multiplier = 1.0
                window = words[max(0, i-2):i]
                for w in window:
                    if w in self.NEGATORS:
                        multiplier *= -1.0
                    elif w in self.INTENSIFIERS:
                        multiplier *= self.INTENSIFIERS[w]

                word_score = val * multiplier
                total_score += word_score
                matches.append({"word": word, "score": round(word_score, 2)})

        # Bounded tanh normalization to [-1.0, 1.0]
        normalized_score = round(math.tanh(total_score / 3.0), 3)

        polarity = "NEUTRAL"
        if normalized_score >= 0.25: polarity = "BULLISH"
        elif normalized_score <= -0.25: polarity = "BEARISH"

        return {
            "sentiment_score": normalized_score,
            "raw_sum": round(total_score, 2),
            "polarity": polarity,
            "matched_terms": matches,
            "word_count": len(words)
        }

    def aggregate_stream(self, news_items: List[Dict[str, Any]], current_time: float = None) -> Dict[str, Any]:
        """
        Aggregates multiple timestamped news items with exponential decay: exp(-lambda * delta_t).
        """
        now = current_time or time.time()
        w_score = 0.0
        tot_weight = 0.0

        for item in news_items:
            t = float(item.get("timestamp", now))
            delta_hours = max(0.0, (now - t) / 3600.0)
            weight = math.exp(-self.decay_lambda * delta_hours)

            score_info = self.score_text(item.get("text", ""))
            w_score += score_info["sentiment_score"] * weight
            tot_weight += weight

        avg_score = round(w_score / max(1e-4, tot_weight), 3) if tot_weight > 0 else 0.0

        return {
            "aggregate_sentiment": avg_score,
            "polarity": "BULLISH" if avg_score >= 0.2 else ("BEARISH" if avg_score <= -0.2 else "NEUTRAL"),
            "items_processed": len(news_items),
            "total_weight": round(tot_weight, 3)
        }

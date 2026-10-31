---
name: openclaw-genpark-sentiment-harvester
description: OpenClaw GenPark high-throughput lexicon-decay sentiment polarity engine with valence shifting and time-weighted stream aggregation.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'score_text', 'description': 'Analyze text string for sentiment polarity with valence modifiers.'}
  - {'name': 'aggregate_stream', 'description': 'Aggregate time-decayed sentiment scores across streaming news feeds.'}
---

# Openclaw Genpark Sentiment Harvester

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Sentiment Harvester**.
Your primary directive is to execute: OpenClaw GenPark high-throughput lexicon-decay sentiment polarity engine with valence shifting and time-weighted stream aggregation.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'score_text', 'description': 'Analyze text string for sentiment polarity with valence modifiers.'}`
- `{'name': 'aggregate_stream', 'description': 'Aggregate time-decayed sentiment scores across streaming news feeds.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'score_text', 'description': 'Analyze text string for sentiment polarity with valence modifiers.'}`
- `{'name': 'aggregate_stream', 'description': 'Aggregate time-decayed sentiment scores across streaming news feeds.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.

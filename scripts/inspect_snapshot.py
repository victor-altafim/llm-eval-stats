"""Olha o formato bruto de um snapshot antes de escrever o parser."""
import json
import sys

from llm_eval_stats.leaderboard.fetch import fetch_snapshot

data = fetch_snapshot(sys.argv[1])

print("chaves do topo:", list(data.keys()))
print("meta:", json.dumps(data["meta"], indent=2))

models = data["models"]
print("quantos modelos:", len(models))
print("chaves de um modelo:", list(models[0].keys()))
print("primeiro modelo:", models[0])
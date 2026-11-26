"""Lexical groundedness check for RAG answers: what share of each answer sentence's content words appear in the retrieved context.
This is a cheap heuristic, not an entailment model: it catches invented details but cannot catch wrong reasoning."""
import re

STOP = set("a an the is are was were of to in on and or for with by as at it its this that be from".split())


def words(t):
    return {w for w in re.findall(r"[a-z0-9]+", t.lower()) if w not in STOP}


def check(answer, context, threshold=0.6):
    ctx = words(context)
    res = []
    for s in re.split(r"(?<=[.!?])\s+", answer.strip()):
        w = words(s)
        score = len(w & ctx) / len(w) if w else 1.0
        res.append((s, round(score, 2), score >= threshold))
    return res

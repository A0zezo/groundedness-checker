# groundedness-checker

Cheap lexical check for RAG answers: for each answer sentence, the share of its content words found in the retrieved context.

## Run

```bash
pip install -r requirements.txt
python demo.py
pytest
```

## Output (reproduced)

```
$ python3 demo.py
GROUNDED    1.0   FastAPI is a Python web framework built on Starlette.
UNSUPPORTED 0.0   It was released by Google in 2010.

$ pytest -q
5 passed in 0.01s
```

## Limits

- A word-overlap heuristic, not an entailment model. It catches invented details but not wrong reasoning or paraphrases that use different words.

from ground import check

context = "FastAPI is a Python web framework. It uses type hints and is built on Starlette and Pydantic."
answer = "FastAPI is a Python web framework built on Starlette. It was released by Google in 2010."
for s, score, ok in check(answer, context):
    print(f"{'GROUNDED' if ok else 'UNSUPPORTED':<12}{score:<6}{s}")

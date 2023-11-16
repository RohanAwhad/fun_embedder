import text_vectorization

from fastapi import FastAPI
from typing import List

app = FastAPI()


@app.get("/embed")
async def embed(text: str) -> List[float]:
    return text_vectorization.vectorize(text).tolist()


@app.get("/embed_batch")
async def embed_batch(text: List[str]) -> List[List[float]]:
    return text_vectorization.vectorize_batch(text).tolist()

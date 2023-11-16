import text_vectorization

from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()


@app.post("/embed")
async def embed(text: str) -> Dict[str, List[float]]:
    return {"embeddings": text_vectorization.vectorize(text).tolist()}


@app.post("/embed_batch")
async def embed_batch(text: List[str]) -> Dict[str, List[List[float]]]:
    return {"embeddings": text_vectorization.vectorize_batch(text).tolist()}

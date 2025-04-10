# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from recommender import get_top_k_recommendations

app = FastAPI(title="SHL Assessment Recommender")

class QueryInput(BaseModel):
    query: str

@app.post("/recommend")
def recommend_assessments(query_input: QueryInput):
    query = query_input.query
    results = get_top_k_recommendations(query)
    return {"recommendations": results}

# app/recommender.py

import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util
from functools import lru_cache

class SHLRecommender:
    def __init__(self, csv_path: str):
        self.df = pd.read_csv(csv_path)

        # Combine relevant fields for semantic search (excluding description)
        self.df['combined_text'] = self.df.apply(
            lambda row: f"{row['assessment_name']} {row['test_type']} "
                        f"{row['remote_testing_support']} {row['adaptive/irt_support']}",
            axis=1
        )

        # Load pre-trained model and encode all assessment entries
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.model.encode(self.df['combined_text'].tolist(), convert_to_tensor=True)

    def recommend(self, query: str, top_k: int = 10):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        similarities = util.cos_sim(query_embedding, self.embeddings)[0]
        top_k_indices = torch.topk(similarities, k=top_k).indices

        recommendations = []
        for idx in top_k_indices:
            row = self.df.iloc[idx.item()]
            score = similarities[idx].item()
            recommendations.append({
                "assessment_name": row["assessment_name"],
                "url": row["url"],
                "remote_testing_support": row["remote_testing_support"],
                "adaptive/irt_support": row["adaptive/irt_support"],
                "test_type": row["test_type"],
                "score": round(score, 4)
            })

        return recommendations

@lru_cache(maxsize=1)
def get_recommender(csv_path="data/final_assessment_catalogue_with_descriptions.csv"):
    return SHLRecommender(csv_path)

def get_top_k_recommendations(query, k=10, csv_path="data/final_assessment_catalogue_with_descriptions.csv"):
    recommender = get_recommender(csv_path)
    return recommender.recommend(query, top_k=k)

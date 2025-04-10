# app/evaluate.py

import streamlit as st
from recommender import get_top_k_recommendations
import pandas as pd

st.set_page_config(page_title="Evaluate Recommendation System", layout="wide")

st.title("🔍 SHL Assessment Recommender Evaluation")

# Example evaluation queries and ground truths (you can expand these!)
test_data = [
    {
        "query": "Looking for leadership assessment for senior managers",
        "expected": ["Leadership Potential", "Executive Leadership"]
    },
    {
        "query": "Need test for graduate-level analytical thinking",
        "expected": ["Graduate Reasoning Test", "Cognitive Ability"]
    },
    {
        "query": "Hiring for customer support, need personality test",
        "expected": ["Customer Service Assessment", "Personality Profile"]
    }
]

results = []

for sample in test_data:
    query = sample["query"]
    expected = sample["expected"]

    recommendations = get_top_k_recommendations(query, k=5)
    recommended_names = [rec["assessment_name"] for rec in recommendations]

    hit_count = sum(1 for name in recommended_names if name in expected)
    precision = hit_count / len(recommended_names)
    recall = hit_count / len(expected)

    results.append({
        "Query": query,
        "Expected": ", ".join(expected),
        "Recommended": ", ".join(recommended_names),
        "Precision": round(precision, 2),
        "Recall": round(recall, 2)
    })

# Show table
df = pd.DataFrame(results)
st.dataframe(df)

# Show overall stats
st.markdown("### 📊 Evaluation Summary")
st.metric("Average Precision", f"{df['Precision'].mean():.2f}")
st.metric("Average Recall", f"{df['Recall'].mean():.2f}")

# app/app.py

import streamlit as st
import pandas as pd
from recommender import get_top_k_recommendations

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
st.title("🔍 SHL Assessment Recommendation Engine")
st.markdown("Enter a job description or query below and get top SHL assessments that match!")

user_input = st.text_area("📝 Enter Job Description or Hiring Requirement:", height=200)
k = st.slider("How many recommendations do you want?", min_value=1, max_value=10, value=5)

if st.button("🔎 Recommend Assessments"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a valid input.")
    else:
        try:
            results = get_top_k_recommendations(user_input, k=k)

            if not results:
                st.info("No relevant assessments found.")
            else:
                display_df = pd.DataFrame(results)

                display_df["assessment_name"] = display_df.apply(
                    lambda row: f"[{row['assessment_name']}]({row['url']})", axis=1
                )

                display_df = display_df[[
                    "assessment_name", "remote_testing_support",
                    "adaptive/irt_support", "test_type", "score"
                ]]
                display_df.columns = [
                    "Assessment Name (Click to View)", "Remote Testing",
                    "Adaptive/IRT", "Test Type", "Match Score"
                ]

                st.success(f"✅ Top {len(display_df)} recommendations found!")
                st.dataframe(display_df, use_container_width=True)

        except Exception as e:
            st.error(f"🚨 An error occurred while fetching recommendations: {e}")

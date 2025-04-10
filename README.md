# SHL Assessment Recommendation System 🔍🧠

This project was developed as part of the SHL Generative AI Internship Assessment. It is a semantic recommendation system that takes a job description or user query and returns the most relevant SHL assessments from their catalog. The goal is to simplify and optimize the hiring process by recommending suitable tests based on role requirements and context.

---

## 🚀 Web App URL

🔗 **[Live Demo]([https://your-streamlit-app-url]([https://shl-assessment-recommender-7fdtz2ncxsgtpscucufkf5.streamlit.app/)](https://shlrecommender-bhrgqfhrvvuhyefmx8srya.streamlit.app/))**  


---

## 📌 Problem Statement

SHL offers a diverse catalog of assessments across job roles, skills, and cognitive traits. Hiring managers often struggle to select the right assessments that match their job descriptions. This project solves that by using **semantic search** to automatically recommend relevant assessments based on natural language input.

---

## 🧠 Approach

- **Data Extraction:** We scraped and cleaned the SHL product catalog to build a usable dataset (`catalog.json`).
- **Semantic Matching:** Used `sentence-transformers` to embed both the input query and catalog assessments into vector space.
- **Similarity Search:** Used cosine similarity to rank and retrieve top-k assessment matches.
- **Evaluation:** Implemented metrics like Recall@K and MAP@K for validation against ground truth.
- **Frontend + API:** Built a Streamlit-based interactive frontend and REST API to serve recommendations.

📄 **[Read 1-Page Approach PDF](https://github.com/MITNIK27/shl-recommender/blob/main/Document.pdf)**

---

## 📂 Project Structure
├── app.py # Streamlit frontend + API logic ├── recommender.py # Semantic similarity + recommendations ├── evaluate.py # Evaluation script ├── data/ │ ├── catalog.json # Parsed assessment data │ └── test_queries.json # Ground truth for evaluation ├── SHL_Assessment_Recommendation_Approach.pdf ├── requirements.txt └── README.md


---

## 🧪 Evaluation

We evaluate using:
- **Recall@K**: Measures if the relevant assessments appear in top-k results.
- **MAP@K**: Mean Average Precision, accounts for ranking quality.

```bash
python evaluate.py

# Clone the repository
git clone https://github.com/your-username/shl-assessment-recommendation.git
cd shl-assessment-recommendation

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py


# 🎬 Movie Recommender System

A content-based movie recommender system built using Python and machine learning that suggests similar movies based on their features, with an interactive Streamlit interface and TMDB API integration.

---

## 🚀 Features
- Recommends movies based on content similarity
- Interactive Streamlit web interface
- Displays movie posters using TMDB API
- Handles missing data and API failures gracefully
- Secure API key handling using environment variables

---

## 🧠 How It Works
- Movie metadata is converted into numerical vectors
- Cosine similarity is used to measure similarity between movies
- The top similar movies are recommended based on the selected movie

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Scikit-learn
- Pandas & NumPy
- TMDB API

---

## 📂 Project Structure
```movie-recommender/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── model/
├── movie_list.pkl
└── similarity.pkl

yaml
Copy code

> ⚠️ Large `.pkl` model files are excluded from the repository due to GitHub file size limits.

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

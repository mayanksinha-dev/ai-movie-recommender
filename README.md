# 🎬 Movie Recommender System

An AI-powered Movie Recommender System built with **Python**, **Streamlit**, and **Machine Learning**. The application recommends similar movies based on content similarity and displays movie posters using the TMDB API.

## 🚀 Features

- 🎥 Recommend 5 similar movies instantly
- 🖼️ Fetch movie posters using TMDB API
- 🔍 Search or select movies from a dropdown
- ⚡ Fast recommendations using cosine similarity
- 🎨 Interactive Streamlit web interface

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Pickle
- Requests
- TMDB API

## 📂 Project Structure

```
movie-recommender-system/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── assets/
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```

### Create a virtual environment (Optional)

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/Mac**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🔑 TMDB API

Create a free account at **The Movie Database (TMDB)** and generate an API key.

Replace your API key inside `app.py`:

```python
api_key = "YOUR_API_KEY"
```

---

## 📸 Screenshots

### Home Page

<img src="assets/home.png" width="900">

### Recommendations

<img src="assets/recommendation.png" width="900">

---

## 🧠 How It Works

1. User selects a movie.
2. The trained similarity matrix finds the closest movies.
3. Movie IDs are used to fetch posters from the TMDB API.
4. Recommended movies and posters are displayed in the Streamlit interface.

---

## 📦 Requirements

- Python 3.10+
- Streamlit
- Pandas
- NumPy
- Requests
- Scikit-learn

Install using:

```bash
pip install -r requirements.txt
```

---

## 🌟 Future Improvements

- User authentication
- Genre-based recommendations
- Search autocomplete
- Movie trailers
- Ratings and reviews
- Hybrid recommendation system
- Deploy on Streamlit Cloud

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request


⭐ If you found this project useful, don't forget to star the repository!
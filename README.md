# 📚 AI Book Recommendation System

An interactive and intelligent **Book Recommendation System** built using **Python**, **Streamlit**, and **Machine Learning**.

This application recommends similar books based on **book titles** and **authors** using **TF-IDF Vectorization** and **Cosine Similarity** algorithms.

The project provides a clean and user-friendly interface where users can search for books and instantly receive personalized recommendations.

---

# 🚀 Features

✅ Smart book recommendations  
✅ Interactive Streamlit web interface  
✅ Machine Learning based recommendation engine  
✅ TF-IDF text vectorization  
✅ Cosine similarity algorithm  
✅ Book cover image display  
✅ Fast and lightweight performance  
✅ Clean and responsive UI  
✅ Real-time recommendation generation  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application framework |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning algorithms |
| TF-IDF Vectorizer | Text feature extraction |
| Cosine Similarity | Recommendation logic |

---

# 📂 Project Structure

```bash
Book-Recommendation-System/
│
├── Book-Recommendation-System.py
├── Books.csv
├── requirements.txt
├── runtime.txt
└── README.md
```

---

# 📊 Dataset Information

The dataset contains book-related information such as:

- ISBN
- Book Title
- Author Name
- Publication Year
- Publisher
- Book Cover Images

The dataset is cleaned and processed before generating recommendations.

---

# ⚙️ How the Project Works

# Step 1 — Load Dataset

The application loads data from:

```python
Books.csv
```

The dataset is read using Pandas.

---

# Step 2 — Data Cleaning

The project performs several preprocessing tasks:

- Removes null values
- Removes duplicate books
- Cleans title and author names
- Optimizes dataset size
- Handles bad lines and encoding issues

---

# Step 3 — Feature Engineering

The recommendation model combines:

```python
Book Title + Author Name
```

Example:

```python
Harry Potter J.K. Rowling
```

This improves recommendation quality.

---

# Step 4 — TF-IDF Vectorization

The text data is converted into numerical vectors using:

```python
TfidfVectorizer()
```

TF-IDF measures the importance of words within the dataset.

---

# Step 5 — Similarity Calculation

The project calculates similarity between books using:

```python
cosine_similarity()
```

Books with higher similarity scores are considered more relevant.

---

# 🧠 Recommendation Algorithm

When a user selects a book:

1. The system searches the selected book
2. Computes similarity scores
3. Finds the most similar books
4. Displays top recommendations

If no exact match is found, random books are displayed.

---

# 🖥️ User Interface

The Streamlit application contains:

- Search dropdown
- Recommendation button
- Recommended books section
- Book cover images
- Author information

---

# 📸 Application Preview

## Main Dashboard

- Search books instantly
- Generate recommendations
- Display similar books
- Show book thumbnails
- Display author names

---

# 📦 Requirements

Install all required libraries using:

```bash
pip install -r requirements.txt
```

---

# 📜 requirements.txt

```txt
streamlit
pandas
numpy
scikit-learn
requests
pillow
```

---

# ▶️ Installation Guide

# 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/book-recommendation-system.git
```

---

# 2️⃣ Navigate to Project Directory

```bash
cd book-recommendation-system
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Run Streamlit Application

```bash
streamlit run Book-Recommendation-System.py
```

---

# 🌐 Deployment Platforms

This project can be deployed on:

- Streamlit Cloud
- Railway
- Render
- Hugging Face Spaces
- Heroku

---

# 📈 Future Improvements

Future upgrades planned for the project:

- User authentication system
- Collaborative filtering
- Hybrid recommendation system
- Genre-based filtering
- Rating-based recommendations
- AI chatbot integration
- Deep learning recommendations
- Voice search functionality
- Personalized user profiles

---

# 📚 Machine Learning Concepts Used

This project demonstrates:

- Natural Language Processing (NLP)
- Text Vectorization
- Feature Engineering
- Similarity Measurement
- Recommendation Systems
- Content-Based Filtering

---

# 🎯 Project Objectives

The main objective of this project is to:

- Build an intelligent recommendation system
- Learn Machine Learning concepts
- Practice NLP techniques
- Develop a real-world AI application
- Create a portfolio-ready project

---

# 💡 Use Cases

This system can be used in:

- Online libraries
- Book-selling platforms
- Educational websites
- AI recommendation engines
- Reading applications
- E-learning systems

---

# 🔥 Key Highlights

✔️ Beginner-friendly AI project  
✔️ Real-world recommendation system  
✔️ Streamlit interactive dashboard  
✔️ Machine Learning integration  
✔️ Portfolio-ready project  
✔️ Easy deployment  

---

# 👨‍💻 Author

## SAUBHAGYA MUNSI

Passionate about:
- Python Development
- Artificial Intelligence
- Machine Learning
- Data Science
- Full Stack Development

---

# 🤝 Contributing

Contributions are welcome.

You can:
- Improve UI
- Add new algorithms
- Optimize recommendation engine
- Improve dataset handling
- Add advanced filtering

---

# ⭐ Support

If you found this project helpful:

⭐ Star this repository  
🍴 Fork this project  
📢 Share with others  

---

# 📜 License

This project is licensed under the MIT License.

---

# 🙌 Acknowledgements

Special thanks to:
- Streamlit
- Scikit-learn
- Pandas
- Open-source contributors

for providing amazing tools and libraries.

---

# 📬 Contact

For suggestions or collaboration:

- GitHub: https://github.com/Saubhagya-M
- LinkedIn: www.linkedin.com/in/saubhagya-munsi-20042012sg

---

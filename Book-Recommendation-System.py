import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Book Recommendation System",
    layout="wide"
)

st.title("📚 AI Book Recommendation System")
st.write("Find similar books based on title and author")


# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    books = pd.read_csv(
        "Books.csv",
        sep=",",
        encoding="latin-1",
        header=None,
        names=[
            "isbn",
            "title",
            "author",
            "year",
            "publisher",
            "image_s",
            "image_url",
            "image_l"
        ],
        on_bad_lines="skip",
        engine="python"
    )

    # Clean data
    books["title"] = books["title"].astype(str).str.strip()
    books["author"] = books["author"].astype(str).str.strip()

    books = books.dropna(subset=["title", "author"])
    books = books.drop_duplicates(subset=["title"])
    books = books.head(10000)

    return books


books = load_data()


# -----------------------------
# Build Recommendation Model
# -----------------------------
@st.cache_data
def build_model(df):
    df_copy = df.copy()

    # Combine title + author
    df_copy["features"] = df_copy["title"] + " " + df_copy["author"]

    # Convert text to vectors
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(df_copy["features"])

    # Similarity matrix
    similarity = cosine_similarity(tfidf_matrix)

    similarity_df = pd.DataFrame(
        similarity,
        index=df_copy["title"],
        columns=df_copy["title"]
    )

    return similarity_df


similarity_df = build_model(books)


# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(book_name):
    if book_name in similarity_df.index:
        recommendations = similarity_df[book_name].sort_values(
            ascending=False
        )[1:6]

        return recommendations.index.tolist()

    return books["title"].sample(5).tolist()


# -----------------------------
# UI
# -----------------------------
book_list = sorted(books["title"].unique())

selected_book = st.selectbox(
    "🔎 Search a book",
    book_list
)

if st.button("Recommend"):
    recommended_books = recommend(selected_book)

    st.subheader("📖 Recommended Books")

    cols = st.columns(5)

    for i, book in enumerate(recommended_books):
        book_data = books[books["title"] == book].iloc[0]

        with cols[i]:
            if pd.notna(book_data["image_url"]):
                st.image(book_data["image_url"], width=140)
            else:
                st.write("📘 No Image")

            st.write(f"**{book}**")
            st.caption(book_data["author"])
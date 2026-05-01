import streamlit as st
import pickle
import re
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity

# Page Config ---
st.set_page_config(page_title="News Recommender", page_icon="📰", layout="centered")

# Initialize Stemmer
ps = PorterStemmer()

# Helper Functions
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)   # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    return " ".join([ps.stem(word) for word in text.split()]) # stemming

@st.cache_resource
def load_models():
    articles = pickle.load(open('articles.pkl', 'rb'))
    cv = pickle.load(open('cv.pkl', 'rb'))
    vector = pickle.load(open('vector.pkl', 'rb'))
    return articles, cv, vector

#  Load Data 
try:
    articles, cv, vector = load_models()
except FileNotFoundError:
    st.error("Model files missing. Please run the pickle export in your notebook first.")
    st.stop()

#  UI Layout 
st.title("📰 AI News Recommender")
st.write("Enter a topic or phrase, and we'll find the most relevant articles for you.")

user_input = st.text_input("Search for news...", placeholder="e.g., Trainer aircraft crashes in Odisha")
top_n = st.slider("Number of articles to recommend", 1, 10, 5)

if st.button("Find Articles"):
    if user_input.strip():
        with st.spinner("Searching..."):
            try:
                #  Clean and Vectorize Input
                processed_text = clean_text(user_input)
                text_vector = cv.transform([processed_text]).toarray()
                
                #  Calculate Similarity
                similarities = cosine_similarity(text_vector, vector).flatten()
                
                # Get Top Indices
                article_indices = sorted(list(enumerate(similarities)), reverse=True, key=lambda x: x[1])[0:top_n]
                
                # Display Results
                st.subheader("Recommended Articles:")
                st.write("---")
                for i in article_indices:
                    row = articles.iloc[i[0]]
                    headline = row['headline']
                    url = row['url']
                    
                    # Markdown link for clickable headline
                    st.markdown(f"#### [{headline}]({url})")
                    st.caption(f"Relevance Score: {round(i[1] * 100, 2)}%")
                    st.write("---")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a search query.")
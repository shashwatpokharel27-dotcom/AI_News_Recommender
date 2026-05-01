# 📰 AI News Recommender

An interactive, AI-powered news recommendation engine. This project uses **Natural Language Processing (NLP)** to analyze articles from the Indian Express, converting text into mathematical vectors to suggest the most relevant news stories based on user interests.

---

## 🖼️ Project Demo

| 1. Default View | 2. Searching for Articles |
|---|---|
| ![Default View](screenshots/default.png) | ![Search View](screenshots/search.png) |
| *The initial state of the application.* | *Inputting a query into the search bar.* |

| 3. Recommendations | 4. Source Redirection |
|---|---|
| ![Recommendations](screenshots/recommendations.png) | ![Redirect](screenshots/redirect1.png)(screenshots/redirect1.png) |
| *Top articles with relevance scores.* | *Redirecting to the official Indian Express site.* |

---

## 📂 Project Structure
AI_News_Recommender/
├── screenshots/               # Folder containing UI demonstration images
├── .gitignore                 # Excludes heavy CSV and PKL files from version control
├── indian_news_article.ipynb  # Jupyter Notebook: Data cleaning, EDA & Model training
├── streamlit_app.py           # Streamlit Web App: The interactive user interface
├── requirements.txt           # Project dependencies
└── readme.md                  # Project documentation (this file)

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/shashwatpokharel27-dotcom/AI_News_Recommender.git
cd AI_News_Recommender

### 2. Create virtual environment
 ```bash   
python -m venv myenv

Activate environment
```bash
myenv\Scripts\activate

Windows:
```bash
myenv\Scripts\activate

Mac/Linux:
```bash
source myenv/bin/activate


### 3. Install dependencies
```bash
pip install -r requirements.txt

## 4. 📊 Dataset & Setup
Due to GitHub's file size limits (the raw dataset is 63MB), the data and the generated model files are not stored directly in this repository. 

1. **Download the Dataset:** [Click here to download News_Articles_Indian_Express.csv](https://drive.google.com/file/d/1UORa4sRzpAc-eSfUSGoh_yc3g-C6Qplx/view?usp=drive_link)
2. **Location:** Place the downloaded `.csv` file inside the `notebooks/project/` folder.
3. **Train the Model:** Run all cells in the `indian_news_article.ipynb` notebook. This will process the data and create the following necessary model files:
    * `articles.pkl` (Processed dataframe)
    * `cv.pkl` (The Vectorizer)
    * `vector.pkl` (The pre-calculated text vectors)

---

4. Run the Web App
Once you have generated the .pkl files from the notebook, start the UI by running:

Bash
streamlit run streamlit_app.py

## 🚀 How it Works
1. **Preprocessing:** Cleans text using Regex and reduces words to their root form using **NLTK's PorterStemmer**.
2. **Vectorization:** Converts text into a bag-of-words model using `CountVectorizer` (capped at 9,000 features).
3. **Similarity Engine:** Calculates the **Cosine Similarity** between your search query and the entire database of articles.
4. **User Interface:** Displays the top results with a **Relevance Score (%)** and direct links to the source articles.

---

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Data Science Libraries:** Pandas, Scikit-learn, NLTK
* **Web Framework:** Streamlit
* **Model Serialization:** Pickle

---



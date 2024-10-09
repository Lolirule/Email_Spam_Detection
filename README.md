# Email/SMS Spam Classifier

## Project Overview
A machine learning-based email spam detection system that classifies incoming emails as spam or not spam, utilizing Natural Language Processing techniques and various machine learning algorithms for accurate filtering.

## Technologies Used
- **Python**
- **Scikit-learn**
- **Natural Language Processing**
- **Streamlit** for the user interface

## Steps Involved
1. **Data Loading and Analysis**: Load data, check for null values, duplicates, and perform exploratory data analysis (EDA) to gain insights.
2. **Feature Engineering**: Tokenize emails and extract features such as number of sentences, words, etc.
3. **Data Preprocessing**: Clean the text by lowering case, removing special characters, stopwords, and applying stemming. Analyze common words and create word clouds.
4. **Model Building**: Implement Naive Bayes models (Gaussian, Bernoulli, Multinomial) using TF-IDF for vectorization, followed by a train-test split.
5. **Model Evaluation**: Compare multiple models (SVC, KNN, Naive Bayes, Decision Trees, etc.) for accuracy and precision.
6. **Voting and Stacking**: Apply voting classifiers and stacking methods; select the best-performing model (Multinomial Naive Bayes).

## How to Run
1. Clone the repository.
2. Install the required packages: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Conclusion
This project provides a robust solution for spam detection, ensuring users maintain a secure inbox with accurate classification.


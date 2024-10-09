import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Download punkt and punkt_tab
nltk.download('punkt')
nltk.download('punkt_tab')

# # Download necessary NLTK resources
# nltk.download('punkt', quiet=True)
# nltk.download('stopwords', quiet=True)
ps = PorterStemmer()

def transform_text(text):
  ##Lowering the letters
  text = text.lower()
  ## Converting them to list
  text = nltk.word_tokenize(text)
  y=[]
  ## Removing special Charachters
  for i in text:
    if i.isalnum():
      y.append(i)
  text =y[:]
  y.clear()
  ## Removing stopping words and punctuation
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)
  text =y[:]
  y.clear()
  ## Stemming the words
  for i in text:
    y.append(ps.stem(i))
  return " ".join(y)
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    #Preprocessing
    transformed_sms = transform_text(input_sms)
    #Vectorizing
    vector_input = tfidf.transform([transformed_sms])
    #Predict
    result = model.predict(vector_input)[0]
    #Display
    if result ==1:
        st.header("Spam")
    else:
        st.header("Not-Spam")

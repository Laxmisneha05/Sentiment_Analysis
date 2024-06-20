import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

# Load the vectorizer and the model
vect = joblib.load('tfidf_vectorizer.pkl')
model = joblib.load('svc_model.pkl')

# Title of the Streamlit app
st.title("Sentiment Analysis App")

# Input text box
review = st.text_area("Enter your review here:")

if st.button("Predict Sentiment"):
    if review:
        # Transform the input review using the loaded vectorizer
        transformed_review = vect.transform([review])

        # Predict the sentiment using the loaded model
        prediction = model.predict(transformed_review)

        # Map the numeric prediction to a sentiment
        sentiment = "Positive" if prediction == 1 else "Negative"
        st.write(f"The review is **{sentiment}**.")
    else:
        st.write("Please enter a review to analyze.")

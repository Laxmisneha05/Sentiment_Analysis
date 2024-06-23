# Sentiment Analysis App
This is a simple sentiment analysis app built using Streamlit. The app uses a pre-trained Linear Support Vector Classifier (SVC) model and TF-IDF vectorizer to classify movie reviews as either positive or negative.

 ## Features
- User-friendly interface for entering movie reviews
- Real-time sentiment prediction (positive/negative)
- Pre-trained model for quick and accurate predictions

## Installation
### Clone the repository:
```
 git clone https://github.com/Laxmisneha05/Sentiment_Analysis.git
```
```
cd Sentiment_Analysis
```
### Install the required dependencies:
```
pip install streamlit scikit-learn joblib pandas matplotlib seaborn wordcloud plotly
```

### Ensure you have the saved model and vectorizer files in the project directory:

- tfidf_vectorizer.pkl
- svc_model.pkl

## Usage
To run the app, use the following command:
```
streamlit run app.py
```

## Project Structure
- app.py: The main Streamlit app file.
- tfidf_vectorizer.pkl: The saved TF-IDF vectorizer.
- svc_model.pkl: The saved SVC model.
- README.md: This file providing an overview of the project.

## Example
After starting the app, you will see a text area where you can enter a movie review. Once you enter the review and click the "Predict Sentiment" button, the app will display whether the review is positive or negative.

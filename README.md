# Resume Screening App

## Overview
This project is a Resume Screening App using Streamlit, TF-IDF vectorization, and a machine learning classifier. The app processes uploaded resumes, extracts text, cleans the data, and predicts the job category based on a trained model.

## Features
- Upload resumes in `.txt` or `.pdf` format.
- Cleans and preprocesses the text to remove unwanted characters.
- Uses TF-IDF vectorization for feature extraction.
- Predicts the job category using a pre-trained machine learning model.
- Displays the predicted job category.

## Requirements
### Software Dependencies:
- Python 3.x
- Streamlit
- NLTK
- Pickle
- Scikit-learn

### Install Dependencies:
```bash
pip install streamlit nltk scikit-learn
```

## Project Structure
```
Resume-Screening-App/
│-- clf.pkl  # Pre-trained classification model
│-- tfidf.pkl  # TF-IDF vectorizer
│-- app.py  # Main Streamlit application
```

## How to Run the Project
1. **Ensure required models are available:**
   - Place `clf.pkl` and `tfidf.pkl` in the project directory.
2. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```
3. **Upload a resume:**
   - The app will process the file and display the predicted job category.

## Notes
- The application supports `.txt` and `.pdf` file formats.
- Ensure that `clf.pkl` and `tfidf.pkl` are trained and correctly stored.
- The app uses a predefined category mapping to return human-readable job categories.


from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load pre-trained model and encoder
model = joblib.load('model.pkl')
encoder = joblib.load('encoder.pkl')
def score_to_grade(avg_score):
    if avg_score >= 90: return 'A (Excellent)'
    elif avg_score >= 80: return 'B (Very Good)'
    elif avg_score >= 70: return 'C (Good)'
    elif avg_score >= 60: return 'D (Needs Improvement)'
    else: return 'F (Work Hard)'
# Grade comments
GRADE_COMMENTS = {
    'A (Excellent)': "Outstanding performance! Keep up the excellent work.",
    'B (Very Good)': "Very good results! You're close to excellence.",
    'C (Good)': "Good performance, but there's room for improvement.",
    'D (Needs Improvement)': "You need to focus more on your studies.",
    'F (Work Hard)': "Serious improvement needed. Please seek extra help."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    student_data = {
        'gender': request.form['gender'],
        'race/ethnicity': request.form['ethnicity'],
        'parental level of education': request.form['parent_edu'],
        'lunch': request.form['lunch'],
        'test preparation course': request.form['test_prep']
    }
    
    # Convert to DataFrame and encode
    student_df = pd.DataFrame([student_data])
    student_encoded = encoder.transform(student_df)
    
    # Make prediction
    score = model.predict(student_encoded)[0]
    grade = score_to_grade(score)
    comment = GRADE_COMMENTS[grade]
    
    return render_template('result.html', 
                         grade=grade, 
                         comment=comment,
                         score=score,
                         student_data=student_data)

if __name__ == '__main__':
    app.run(debug=True)
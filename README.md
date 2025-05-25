# Student Performance Prediction App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0%2B-orange)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-brightgreen)

A web application that predicts student grades based on demographic and academic factors, with interactive data visualizations.

## Features

- **Grade Prediction**: Predicts student performance (A/B/C/D/F) using machine learning
- **Data Visualization**: Interactive charts showing performance patterns
- **Responsive Design**: Works on both desktop and mobile devices
- **Educational Insights**: Provides feedback comments for each grade level
## File Structure
student-performance-predictor/
├── app.py                 # Flask application
├── model.pkl              # Trained ML model
├── encoder.pkl            # Feature encoder
├── requirements.txt       # Dependencies
├── static/
│   └── style.css          # CSS styles
├── templates/
│   ├── index.html         # Homepage
│   ├── result.html        # Results page
│   └── analysis.html      # Visualization page
└── StudentsPerformance.csv # Sample dataset

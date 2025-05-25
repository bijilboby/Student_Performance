# Student Performance Prediction App

A Flask web application that predicts student grades (A/B/C/D/F) using machine learning and provides data visualizations.

## Features

- Predicts student performance based on 5 key factors
- Provides personalized feedback for each grade level
- Shows interactive data visualizations
- Simple, user-friendly interface

## How It Works

1. **Input Student Data**:
   - Users fill out a form with:
     - Gender (Male/Female)
     - Race/Ethnicity (Groups A-E)
     - Parental education level
     - Lunch type (Standard/Free-Reduced)
     - Test preparation status

2. **Machine Learning Prediction**:
   - Random Forest model processes the inputs
   - Predicts one of five grade categories:
     - A (Excellent): ≥90%
     - B (Very Good): 80-89%
     - C (Good): 70-79%
     - D (Needs Improvement): 60-69%
     - F (Work Hard): <60%

3. **Results Display**:
   - Shows predicted grade with color-coded border
   - Provides constructive feedback based on grade
   - Displays all input data for verification

4. **Data Analysis** (Optional):
   - Visualizes grade distribution (pie chart)
   - Compares average scores by gender (bar chart)
   - Shows test preparation impact (bar chart)

## Technical Implementation

### Backend
- **Framework**: Flask
- **Machine Learning**:
  - Algorithm: Random Forest Classifier
  - Accuracy: ~92.5%
  - Features: One-Hot Encoded categorical variables
- **Visualization**: Matplotlib plots rendered as base64 images

### Frontend
- HTML5 with Jinja2 templating
- CSS for responsive design
- No JavaScript dependencies

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/student-performance-predictor.git
cd student-performance-predictor

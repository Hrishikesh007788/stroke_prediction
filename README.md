# Stroke Risk predictor

![alt text](https://els-jbs-prod-cdn.jbs.elsevierhealth.com/cms/attachment/6c1a730a-9ceb-4bf7-a77e-19f55abf1227/fx1_lrg.jpg)


## Problem Statement:

About 15 million people suffer from a stroke per year. It generally occurs due to Age, poor lifestyle and improper habits. 

## Proposed Solution:

A possible solution would be to create a Machine Learning model which would predict whether the person is a risk of future strokes, given their clinical features.  

## Data Description:

Dataset available in kaggle: [Link](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset)

Sources:
Source is kept confidential.

Attribute Information:
1) id: unique identifier
2) gender: "Male", "Female" or "Other"
3) age: age of the patient
4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
6) ever_married: "No" or "Yes"
7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
8) Residence_type: "Rural" or "Urban"
9) avg_glucose_level: average glucose level in blood
10) bmi: body mass index
11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
12) stroke: 1 if the patient had a stroke or 0 if not
*Note: "Unknown" in smoking_status means that the information is unavailable for this patient

## Project Tree Structure
```
 .
├── Analysis
    ├── EDA.ipynb
    ├── Model_selection.ipynb
├── Datasets
     ├── healthcare-dataset-stroke-data.csv
     ├── preprocessed.csv
├── __pycache__
     ├── app.cpython-38.pyc
├── models
     ├── rf.sav
     ├── scaler.pkl
├── src
     ├── model_creation.py
     ├── preprocessing.py
├── templates
     ├── home.html
     ├── nostroke.html
     ├── stroke.html
├── Procfile
├── README.md
├── app.py
└── requirements.txt
```

## Tools used:

- Programming language : Python
- IDE : Visual Studio Code
- Visualization : Matplotlib and Seaborn
- Deployment platform : Heroku
- Front end development : HTML/CSS
- Back end development : Flask
- Version control system : GitHub

## Web App:

Web App Link: https://stroke-predict-app.herokuapp.com

In this web app, we just need to enter 10 clinical features about the person and the algorithm will predict if the person is at a risk of stroke.

## Creator:

1. [Hrishikesh Dutta](https://www.linkedin.com/in/hrishikesh-dutta-6776321a0)



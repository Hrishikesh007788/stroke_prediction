import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
data_preprocessed = pd.read_csv("Datasets/preprocessed.csv")
y = data_preprocessed['stroke']
x = data_preprocessed.drop(['stroke'],axis=1)
from sklearn.preprocessing import StandardScaler
std = StandardScaler()
std.fit(x)
x_scaled = std.transform(x)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=365)
from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=2)
x_train_res, y_train_res = sm.fit_resample(x_train, y_train.ravel())
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(criterion= 'entropy', n_estimators= 200, random_state= 0)
classifier.fit(x_train_res, y_train_res)
import pickle
import os
scaler_path=os.path.join('/Users/hrishikeshdutta/Desktop/Stroke_Prediction','models/scaler.pkl')
with open(scaler_path,'wb') as scaler_file:
    pickle.dump(std,scaler_file)
import joblib
model_path=os.path.join('/Users/hrishikeshdutta/Desktop/Stroke_Prediction/','models/rf.sav')
joblib.dump(classifier,model_path)
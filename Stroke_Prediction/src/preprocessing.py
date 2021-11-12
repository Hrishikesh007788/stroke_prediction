import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
raw_data = pd.read_csv('Datasets/healthcare-dataset-stroke-data.csv')
data = raw_data.drop(['id'],axis=1)
data = data.dropna(axis=0)
data = data.drop(3116)
from sklearn.preprocessing import LabelEncoder
enc=LabelEncoder()
gender=enc.fit_transform(data['gender'])
smoking_status=enc.fit_transform(data['smoking_status'])
work_type=enc.fit_transform(data['work_type'])
Residence_type=enc.fit_transform(data['Residence_type'])
ever_married=enc.fit_transform(data['ever_married'])
data['work_type']=work_type
data['ever_married']=ever_married
data['Residence_type']=Residence_type
data['smoking_status']=smoking_status
data['gender']=gender
data_preprocessed = data
data_preprocessed.to_csv('Datasets/preprocessed.csv', index=False)
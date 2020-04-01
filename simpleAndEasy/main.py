import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
import numpy as np
from sklearn.metrics import r2_score
#loading data

Train_data=pd.read_csv(os.path.join(r'dataset\train.csv'))
Test_data=pd.read_csv(os.path.join(r'dataset\test.csv'))


#EDA
Train_data.head()

sns.distplot(Train_data.y,hist=False)
sns.distplot(Test_data.y,hist=False)

plt.scatter(Train_data.x,Train_data.y,c='r',marker='x')
Train_data.isna().sum()
Train_data=Train_data.dropna()
#predictions
model=linear_model.LinearRegression(normalize=True)
X=Train_data[['x']].as_matrix()
Y=Train_data[['y']].as_matrix()
model.fit(X,Y)

y_pred=model.predict(Test_data[['x']].as_matrix())

print('accuracy of system is ',r2_score(Test_data[['y']].as_matrix(),y_pred))
plt.scatter(Test_data.x,Test_data.y,marker='x')
plt.scatter(Test_data.x,y_pred,marker='o')

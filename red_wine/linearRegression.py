import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
#Loading Data
checker=False
file_link=os.path.join("data_set\winequality-red.csv")
main_data=pd.read_csv(file_link)

main_data.head(10)

main_data.info()

print(main_data.isna().sum())

#EDA
main_data.corr()
sns.heatmap(main_data.corr(),annot=True,fmt='.1g',cmap='coolwarm')


#okay lets see plots

main_data.columns
if(checker==True):
  for i in main_data.columns:
    for j in main_data.columns:  
      sns.scatterplot(main_data[i],main_data[j])
      plt.show()
correlations = main_data.corr()['quality'].drop('quality')
print(correlations)

#Normalizing all quantities
import sklearn.preprocessing as pp
import sklearn.model_selection as ms
import numpy as np
X=pp.normalize(main_data[main_data.columns[0:-1]])

print(X.shape)
Y=np.asarray(main_data[main_data.columns[-1]])
print(Y.shape)

X_train,X_test,Y_train,Y_test=ms.train_test_split(X,Y,test_size=0.33,random_state=40)
X_train.shape
Y_train.shape

import sklearn.linear_model as lm

model=lm.LinearRegression()

model.fit(X_train,Y_train)

y_pred=model.predict(X_test)

import sklearn.metrics as m

m.mean_squared_error(Y_test,y_pred)
X_train[1]

main_data

# displaying coefficients of each feature
features=main_data.columns[0:-1]
coeffecients = pd.DataFrame(model.coef_,features) 
coeffecients.columns = ['Coeffecient'] 
print(coeffecients)

plt.scatter(range(len(y_pred)),y_pred)
plt.scatter(range(len(y_pred)),Y_test)



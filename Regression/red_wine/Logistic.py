import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import sklearn.model_selection as ms
from sklearn.linear_model import LogisticRegression
#Loading Data
checker=False
file_link=os.path.join("data_set\winequality-red.csv")
main_data=pd.read_csv(file_link)

main_data.head(10)

main_data.info()

print(main_data.isna().sum())

ss=StandardScaler()

X_train,X_test,Y_train,Y_test=ms.train_test_split(main_data[main_data.columns[0:-1]],main_data[main_data.columns[-1]],test_size=0.25)

X_train.shape
Y_train.shape

X_train=ss.fit_transform(X_train)
X_test=ss.fit_transform(X_test)

model=LogisticRegression(max_iter=1000)
model.fit(X_train,Y_train)

model.score(X_test,Y_test)

y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(Y_test,y_pred)
accuracy=accuracy_score(Y_test,y_pred)
data=main_data
#Okay accuracy is low around 0.6
#lets divide quality as fine good and bad
for i in range(len(main_data)):
    if main_data.iloc[i,11]>=6:
        data.iloc[i,11]='good'
    else:
        data.iloc[i,11]='bad'
data['quality'].hist()

from sklearn.preprocessing import LabelEncoder
labelencdoer=LabelEncoder()
data['quality']=labelencdoer.fit_transform(data['quality'])



model2=LogisticRegression()
X_train,X_test,Y_train,Y_test=ms.train_test_split(data[data.columns[0:-1]],data[data.columns[-1]],test_size=0.25)
model2.fit(X_train,Y_train)
model2.score(X_test,Y_test)
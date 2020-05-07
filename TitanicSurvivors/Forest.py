import pandas as pd
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,StackingClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
#lets try by droppeing nan age

df.isnull().sum()
data=df[~df['Age'].isnull()]
data.isnull().sum()
data.info()

data['Cabin'].unique()

data['Cabin_Class']=data['Cabin'].str[0]
data['Cabin_Class'].unique()
data=pd.concat([data,pd.get_dummies(data['Cabin_Class'])],axis=1)
data['Sex']=pd.get_dummies(data['Sex'])
data=pd.concat([data,pd.get_dummies(data['Embarked'])],axis=1)
data=pd.concat([data,pd.get_dummies(data['Cabin_Class'])],axis=1)
data=pd.concat([data,pd.get_dummies(data['Pclass'])],axis=1)

#okay i will drop few columns
data.columns
droper=['PassengerId','Pclass','Name','Cabin','Embarked','Cabin_Class']

data=data.drop(droper,axis=1)
X=data[data.columns[1:data.shape[1]]]
Y=data[data.columns[0]]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33)
score_list={}
model=RandomForestClassifier(n_estimators=10,n_jobs=15)
model.fit(X_train,Y_train)
model.score(X_test,Y_test)
score_list.update({'RandomForest':model.score(X_test,Y_test)})
model2=SVC()
model2.fit(X_train,Y_train)
model2.score(X_test,Y_test)
score_list.update({'SVM':model2.score(X_test,Y_test)})

model3=AdaBoostClassifier(n_estimators=15)
model3.fit(X_train,Y_train)
y_hat=model3.predict(X_test)
score_list.update({"AdaBoostDescionTree":model3.score(X_test,Y_test)})

#okay so Ada is best
score_list

#as test set contains Age with null values need to fill them
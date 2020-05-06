import pandas as pd
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder  as OHE
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
labels=df.columns
df.isnull().sum()
X_labels=['Sex','SibSp','Parch','Fare'] 



AgeStudy=df

AgeStudy[~AgeStudy['Age'].isnull()].hist()
for po in df.columns:
    print(po)
    AgeStudy[AgeStudy['Age'].isnull()][po].plot.bar()
AgeStudy.corr()

X=AgeStudy[~AgeStudy['Age'].isnull()]
X.isnull().sum()
X.corr()
X['Embarked']=X['Embarked'].astype('category')
X=pd.concat([X,pd.get_dummies(X['Embarked'])],axis=1)
X.drop('Embarked',axis=1,inplace=True)
X['Sex']=pd.get_dummies(X['Sex'])


X.drop(['PassengerId','Survived','Cabin'],axis=1,inplace=True)
X=pd.concat([X,pd.get_dummies(X['Pclass'])],axis=1)
X.drop('Pclass',axis=1)
X.hist()
X['Name'].str.split().str[1].unique()
changer={}
X[X['Name'].str.split().str[1]=='Col.']



for c in X['Name'].str.split().str[1].unique():
    if c in ['Miss.', 'Master.']:
        continue
    changer.update({c:'rest'})

X['name suffix']=X['Name'].str.split().str[1]

X['name suffix']=X['name suffix'].replace(changer)
X=pd.concat([X,pd.get_dummies(X['name suffix'])],axis=1)

X.corr()

Y=X['Age']
X.drop(['Age'],axis=1,inplace=True)
X.drop(['Name'],axis=1,inplace=True)
X.drop(['name suffix'],axis=1,inplace=True)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33)

X_train
model=LinearRegression(normalize=True,n_jobs=5)
model.fit(X_train,Y_train)
y_hat=model.predict(X_test)
model.score(X_test,Y_test)

plt.scatter(range(1,len(Y_test)+1),Y_test)
plt.scatter(range(1,len(Y_test)+1),y_hat)


#SO accuracy is low cant use it


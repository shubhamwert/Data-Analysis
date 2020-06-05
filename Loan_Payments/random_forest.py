from sklearn.ensemble import RandomForestClassifier
from eda import *
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

columns=df.columns

X=df[['Principal', 'terms', 'past_due_days', 'age','Gender']]
X = pd.concat([X,pd.get_dummies(df['education'])], axis=1)
X['Gender'].replace(to_replace=['male','female'], value=[0,1],inplace=True)
X = preprocessing.StandardScaler().fit(X).transform(X)
Y=df['loan_status'].values

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=4)
print ('Train set:', X_train.shape,  y_train.shape)
print ('Test set:', X_test.shape,  y_test.shape)


testResults={}
#lets begin the tests
#Random Forest


model=RandomForestClassifier()
model.fit(X_train,y_train)
y_hat=model.predict(X_test)

print("accuracy of random forest is ",accuracy_score(y_test,y_hat))
testResults.update({'randomforest':accuracy_score(y_test,y_hat)})

#K clustering

#deciding value of k
k=5

kNN_model = KNeighborsClassifier(n_neighbors=k).fit(X_train,y_train)
kNN_model.fit(X_train,y_train)

y_pred=kNN_model.predict(X_test)

print(sum(y_test==y_pred))
print("accuracy of svm is ",kNN_model.score(X_test,y_test))
testResults.update({'K_mean Clustering':kNN_model.score(X_test,y_test)})

#SVM
model=SVC()
model.fit(X_train,y_train)
print("SVM HAS SCORE",model.score(X_test,y_test))
testResults.update({'svm':model.score(X_test,y_test)})

print(testResults)

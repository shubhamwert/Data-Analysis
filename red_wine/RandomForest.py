import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import sklearn.model_selection as ms
import numpy as np
from sklearn.ensemble import RandomForestClassifier
#THere is a low correlation between various features and hence we wil also try Random Forest

checker=False
file_link=os.path.join("data_set\winequality-red.csv")
main_data=pd.read_csv(file_link)

main_data.head(10)

main_data.info()
#encodings
data=main_data
for i in range(len(main_data)):
    if main_data.iloc[i,11]>=6:
        data.iloc[i,11]='good'
    else:
        data.iloc[i,11]='bad'
data['quality'].hist()

from sklearn.preprocessing import LabelEncoder
labelencdoer=LabelEncoder()
data['quality']=labelencdoer.fit_transform(data['quality'])



model2=RandomForestClassifier(n_estimators=1000)
X_train,X_test,Y_train,Y_test=ms.train_test_split(data[data.columns[0:-1]],data[data.columns[-1]],test_size=0.25)
model2.fit(X_train,Y_train)
model2.score(X_test,Y_test)
y_pred=model2.predict(X_test)
np.dot((Y_test-y_pred),(Y_test-y_pred)).sum()/len(Y_test)
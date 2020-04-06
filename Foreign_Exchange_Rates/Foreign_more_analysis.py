import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
#Load the data
main_data=pd.read_csv('dataSet\Foreign_Exchange_Rates.csv')
main_data[main_data.columns[1]]=pd.to_datetime(main_data[main_data.columns[1]])



#data analysis
main_data.head()

main_data.isna().sum()

main_data.shape

main_data.info()


main_data.describe()

main_data.columns

main_data[main_data.columns[1]].value_counts()
main_data=main_data.replace('ND',np.nan)
main_data = main_data.bfill().ffill() 
#proper conversions to float data type
for k in range(2,main_data.shape[1]):

    main_data[main_data.columns[k]]=pd.to_numeric(main_data[main_data.columns[k]])
main_data.info()

main_data.corr()

sns.heatmap(main_data.corr())



#So there is a corr between different currencies

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
model=RandomForestRegressor(n_estimators=1000)
X=main_data[main_data.columns[2:-1]].as_matrix()
Y=main_data[main_data.columns[-1]].as_matrix()
X_train,X_test,Y_tran,Y_test=train_test_split(X,Y,test_size=0.33)
model.fit(X_train,Y_tran)

model.score(X_test,Y_test)


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
df=pd.read_csv('data/Train/Train.csv',parse_dates=['saledate'])

df.head()

df.columns

df['yearsold']=df.saledate.dt.year
df['monthsold']=df.saledate.dt.month

df.SalePrice=np.log(df.SalePrice)
for i in df.columns:
    print(i)
    if df[i].dtype == 'O':
        print(df[i].unique())
        df[i]=df[i].astype('category')
    print('__'*20)
df.info()
df.UsageBand.cat.codes
df.drop(['saledate','SalesID','auctioneerID'],axis=1,inplace=True)
df['MachineHoursCurrentMeter']=df['MachineHoursCurrentMeter'].fillna(0)
for i in df.columns:
    if df[i].dtype.name == 'category':
        print(df[i].cat.categories)
        df[i].cat.set_categories(list(df[i].cat.categories), ordered=True, inplace=True)
        df[i] = df[i].cat.codes
        print('__'*20)
m=RandomForestRegressor(n_jobs=-1,n_estimators=10,oob_score=True,)
X_train,X_test,Y_train,Y_test=train_test_split(df.drop(['SalePrice'],axis=1),df['SalePrice'],test_size=0.40)
m.fit(X_train,Y_train)
m.score(X_test,Y_test)


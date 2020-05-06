import pandas as pd
#lets try by droppeing nan age

df.isnull().sum()
data=df[~df['Age'].isnull()]
data.isnull().sum()
data.info()

data['Cabin'].unique()

data['Cabin_Class']=data['Cabin'].str[0]
data['Cabin_Class'].unique()
pd.concat([data,pd.get_dummies(data['Cabin_Class'])],axis=1)

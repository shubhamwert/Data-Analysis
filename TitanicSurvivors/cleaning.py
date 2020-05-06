import pandas as pd

df=pd.read_csv('data/train.csv')

df.head()
df.Pclass.unique()
df['Pclass']=df['Pclass'].astype('category')
df['Sex']=df['Sex'].astype('category')
df.drop(['Ticket'],axis=1,inplace=True)
df['Age']=df['Age'].astype(int)
df.info()
df.isnull().sum()
df['Embarked'].dropna(how='any', inplace=True)


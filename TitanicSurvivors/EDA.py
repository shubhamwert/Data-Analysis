import pandas as pd
from random import randint

df=pd.read_csv('data/train.csv')

df.columns
df.describe()

df.info()

df.head(10)


df.isnull().sum()

#so Age and cabin have nan 
# for cabin

df[df['Cabin'].isnull()][df['Survived']==0]
df[df['Cabin'].isnull()][df['Survived']==1]

df['Cabin'].unique()
df[df['Cabin'].isnull()]['Fare']
len(df)

#Embarked 
df['Embarked'].unique()

#df Cabins analysis
df[df['Cabin'].isnull()].describe()
df[~df['Cabin'].isnull()].describe()


df[df['Age'].isnull()]
df['Embarked']
df.corrwith(df['Age'])
df['Age']=df.groupby('SibSp')
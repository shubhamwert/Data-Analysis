import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt

#Loading data
data=pd.read_csv(os.path.join('Data','avocado.csv'))


#functions
def getRegionalAnalysisType(data,region,param):
    organic_only=data[data['type']=='organic']
    not_organic=data[data['type']!='organic']

    region_wise_organic=organic_only[organic_only['region']==region]
    region_wise_not_organic=not_organic[not_organic['region']==region]


    sns.lineplot(region_wise_organic['Date'],region_wise_organic[param])
    
    sns.lineplot(region_wise_not_organic['Date'],region_wise_not_organic[param])
    plt.legend(['organic','conventional'])
    
    plt.title(region)
    plt.show()
#data analysis starting and cleaning
data.head(10)

data.info()
data.describe()
data.drop(data.columns[0],axis=1)
data.dtypes

data['Date']=pd.to_datetime(data['Date'])

#Okay planning a selling plan region wise
#Total income

df=data
df['net income']=df['AveragePrice']*df['Total Volume']

regions=df['region'].unique()

for r in regions:
    getRegionalAnalysisType(df,r,'net income')
for r in regions:
    getRegionalAnalysisType(df,r,'AveragePrice')
bags=['Total Bags','Small Bags','Large Bags']
df[bags]
for r in regions:
    for bag in bags:
        getRegionalAnalysisType(df,r,bag)

    
#BagSize
SizedBags=df[['Date','AveragePrice','Total Bags','Small Bags','Large Bags','type','region']]
SizedBags.describe()
regionalBagsTotal=SizedBags.groupby(['region']).sum()
regionalBagsTotal.drop(['AveragePrice'],axis=1).sort_values('Total Bags',axis=0).plot.bar()
regionalBagsTotal.drop(['AveragePrice'],axis=1).sort_values('Total Bags',axis=0).tail(6).plot.bar()
regionalBagsTotal.drop(['AveragePrice'],axis=1).sort_values('Total Bags',axis=0).head(11).plot.bar()

regionalBagsTotal.drop(['AveragePrice'],axis=1).sort_values('Large Bags',axis=0).plot.bar()
regionalBagsTotal.drop(['AveragePrice'],axis=1).sort_values('Large Bags',axis=0).tail(6).plot.bar()
regionalBagsTotal.drop(['AveragePrice'],axis=1).sort_values('Large Bags',axis=0).head(11).plot.bar()

regionalBagsTotal[regionalBagsTotal['Small Bags']<regionalBagsTotal['Large Bags']]

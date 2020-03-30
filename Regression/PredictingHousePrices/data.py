import pandas as pd
import numpy as np
import seaborn as sns
main_data=pd.read_csv(r'dataset\house-prices-advanced-regression-techniques(1)\train.csv')

main_data.head(10)
main_data.columns

main_data.info()
main_data.describe()
print(main_data.isnull().sum())

print(main_data.corr())

AlleyTypes=main_data['Alley'].unique()
AlleyDict={}
num=0
for Alley in AlleyTypes:
    AlleyDict.update({Alley:num})
    num=num+1
main_data.Alley=main_data.Alley.fillna('unknown')

main_data.Alley= [AlleyDict[item] for item in main_data.Alley]
sns.heatmap(main_data)
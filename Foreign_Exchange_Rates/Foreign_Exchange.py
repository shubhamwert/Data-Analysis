import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

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

#so we only have one value per date
#counter for plot size
#plot for each country
print('plot is not on same scales\nanalyzing...')
i=500
for k in range(2,main_data.columns.shape[0]):
    plt.plot(main_data[main_data.columns[1]].head(i),main_data[main_data.columns[k]].head(i))
    plt.title(main_data.columns[k])
    plt.show()
print("most recent trends")
for k in range(2,main_data.columns.shape[0]):
    plt.plot(main_data[main_data.columns[1]].tail(i),main_data[main_data.columns[k]].tail(i))
    plt.title(main_data.columns[k])
    
plt.legend(main_data.columns[2:main_data.columns.shape[0]])

#only considering few contries
print(main_data.columns)

countries=['Time Serie','CANADA - CANADIAN DOLLAR/US$', 'CHINA - YUAN/US$',
       'HONG KONG - HONG KONG DOLLAR/US$', 'INDIA - INDIAN RUPEE/US$']

smaller_dataSet=main_data[countries].copy()


smaller_dataSet.info()

smaller_dataSet.describe()
print("trends review ")
for k in range(1,smaller_dataSet.columns.shape[0]):
    plt.plot(smaller_dataSet[smaller_dataSet.columns[0]].tail(i),smaller_dataSet[smaller_dataSet.columns[k]].tail(i))
    plt.title(smaller_dataSet.columns[k])
    
plt.legend(smaller_dataSet.columns[1:smaller_dataSet.columns.shape[0]])

#lets group them by year to see yearly trend

yearly_data=main_data.groupby(main_data['Time Serie'].dt.year).mean()
for k in range(0,yearly_data.columns.shape[0]):
    plt.plot(yearly_data[yearly_data.columns[k]].tail(i))
    plt.title(yearly_data.columns[k])
    plt.show()


#TODO apply LSTM using keras
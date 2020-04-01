import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
main_data=pd.read_csv('dataset\sars-outbreak-2003-complete-dataset\sars_2003_complete_dataset_clean.csv')
#i have cumulative means total till that date
#basic data analysis

main_data.head(10)

main_data.shape

main_data.info()
main_data['Date']=pd.to_datetime(main_data['Date'])

main_data.info()

main_data.describe()

#lets have some explolatory data analysis

#data for each country

print("countries in dataset\n",main_data['Country'].unique())
data_in_countries=main_data.groupby(main_data['Country']).max()

data_in_countries_groups=main_data.groupby(main_data['Country'])
data_in_countries=data_in_countries.drop(['Date'],axis=1)
data_in_countries.plot.bar()


print("countries with actual deaths or case ")
data_in_countries_non_zero_deaths=data_in_countries[data_in_countries['Number of deaths'].values>0]
data_in_countries_non_zero_deaths.hist()
data_in_countries_non_zero_deaths.plot.bar()

#few extra columns we are gonna add
data_in_countries_non_zero_deaths['death_per_case']=data_in_countries_non_zero_deaths['Number of deaths']/data_in_countries_non_zero_deaths['Cumulative number of case(s)']

data_in_countries_non_zero_deaths['recoverred_per_death']=data_in_countries_non_zero_deaths['Number recovered']/data_in_countries_non_zero_deaths['Number of deaths']
data_in_countries_non_zero_deaths['recoverred_per_death'].plot.bar()


#so there is a diffrence between recovered and dead vs total cases. 
data_in_countries['unknown_situation_patients']=data_in_countries['Cumulative number of case(s)']-data_in_countries['Number of deaths']-data_in_countries['Number recovered']

data_in_countries['unknown_situation_patients'].plot.bar()

#datewise analysis

data_in_dates_groups=main_data.groupby(main_data['Date'])
data_in_dates=data_in_dates_groups.sum()
data_in_dates.plot()
#also recovered patients
data_in_dates['Cumulative number of case(s)'].plot()
(data_in_dates['Cumulative number of case(s)']-data_in_dates['Number recovered']).plot()
print('above graph is bell shaped, ie most recovered patients were in middle, meaning  ')

#So china has most cases
chinese_data=main_data[main_data['Country'].str.contains("China")]

chinese_by_country=chinese_data.groupby(['Country']).max()
chinese_by_country=chinese_by_country.drop(['Date'],axis=1)
chinese_by_country.plot.bar()

china_mainland=main_data[main_data['Country']=='China']
china_mainland.drop(['Country'],axis=1)

plt.bar(china_mainland['Date'],china_mainland['Cumulative number of case(s)'])
plt.plot(china_mainland['Date'],china_mainland['Number recovered'],color='g')
plt.plot(china_mainland['Date'],china_mainland['Number of deaths'],color='r')
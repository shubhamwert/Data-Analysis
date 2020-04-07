import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('data/loandata/Loan payments data.csv')

df.head()
df['past_due_days']=df['past_due_days'].fillna(0)

df.info()


loan_status=df['loan_status'].unique()

df['Principal'].hist()

df.columns

df.describe()

#So we have 3 loan status

print(loan_status)

df['loan_status'].hist()

#okay so many paid there loan. few are still paying and nearly 100 people 
# we have to do effort
# 
df[df['loan_status']==loan_status[2]] 

#okay so pastd due can help us find defactors or late laon givers
df['age'].hist()

#okay basically 
sns.distplot(df['age'])

#So most people are of age 25 to 35 who take loan
df['education'].hist()

#So college require highest loan

total_loan=df.groupby(['education'],axis=0).sum()['Principal']
plt.pie(total_loan,labels=['Bechalor','High School or Below','Master or Above','college'])
plt.pie(df.groupby(['Gender','education'],axis=0).sum()['Principal'])
labels=df.groupby(['Gender','education'],axis=0)
df.groupby(['Gender','education'],axis=0).sum()['Principal'].plot.pie()
#male takes more loan



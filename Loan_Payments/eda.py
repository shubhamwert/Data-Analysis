import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('data/loandata/Loan payments data.csv')

df.head()


df[df['past_due_days'].isnull()]

#So whoever paid the loan is time has past_due_date =na
df['past_due_days']=df['past_due_days'].fillna(0)

df.info()


loan_status=df['loan_status'].unique()

df['Principal'].hist()

df.columns

df.describe()
df.isnull().sum()

df[df['paid_off_time'].isnull()==True]
#So basically if money is not collected paid_off_time is NaT
df['loan_status']=df['loan_status'].astype('category')
df['education']=df['education'].astype('category')
df['Gender']=df['Gender'].astype('category')

date_columns=['effective_date','due_date','paid_off_time']

for columns in date_columns:
    df[columns]=pd.to_datetime(df[columns])
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
labels=df.groupby(['Gender','education'],axis=0)
df.groupby(['Gender','education'],axis=0).sum()['Principal'].plot.pie()
#male takes more loan

#now lets see we are late on loan and hasnt yet paid it

df[df['paid_off_time'].isna() & df['past_due_days']>0] 
df[df['paid_off_time'].isna() & df['past_due_days']>0].hist() 

print("MONEY IN JEOPARDY:\n",df[df['paid_off_time'].isna() & df['past_due_days']>0]['Principal'].sum())

print("current difference in total money given and unpaid loans",df['Principal'].sum()-df[(df['paid_off_time'].isna() & df['past_due_days']>0)]['Principal'].sum())
print("paid loan ratio not paid load",df[(df['paid_off_time'].isna() & df['past_due_days']>0)]['Principal'].sum()/df[~(df['paid_off_time'].isna() & df['past_due_days']>0)]['Principal'].sum())
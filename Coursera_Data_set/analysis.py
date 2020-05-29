import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_org=pd.read_csv('data/coursea_data.csv')

df_org.head()

df_org.isnull().sum()
df_org.info()
df_org.groupby(['course_title'],axis=1).sum()
for i in ['course_difficulty','course_organization','course_Certificate_type']:
    df_org[i]=df_org[i].astype('category')
# df_org['course_students_enrolled']=df_org['course_students_enrolled'].astype(int)

df_org['course_students_enrolled']=df_org['course_students_enrolled'].str.replace('k','')
df_org['course_students_enrolled']=df_org['course_students_enrolled'].str.replace('m','')

df_org['course_students_enrolled']=df_org['course_students_enrolled'].astype(float)
df_org['course_students_enrolled']=df_org['course_students_enrolled']*1000
df_org.hist()
df_org.groupby(['course_organization'],axis=0)['Id'].count()
s_enroll_num=df_org.nlargest(8,'course_students_enrolled')
s_enroll_num
plt.figure(figsize=(20,10))
ax = sns.barplot(x='course_title', y='course_students_enrolled', data=s_enroll_num)
plt.show()
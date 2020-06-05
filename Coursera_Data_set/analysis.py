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

df_org['course_students_enrolled']=df_org['course_students_enrolled'].str.replace('k','000')
df_org['course_students_enrolled']=df_org['course_students_enrolled'].str.replace('m','0'*6)

df_org['course_students_enrolled']=df_org['course_students_enrolled'].astype(float)
df_org['course_students_enrolled']=df_org['course_students_enrolled']*1000

df_org.hist()
df_org.groupby(['course_organization'],axis=0)['Id'].count()
s_enroll_num=df_org.nlargest(8,'course_students_enrolled')
s_enroll_num
plt.figure(figsize=(20,10))
ax = sns.barplot(x='course_title', y='course_students_enrolled', data=s_enroll_num)
plt.show()
#Course Titles containg particualr courses
data_courses=pd.DataFrame()
courses=['Data Science','Arts','Deep Learning','English','Spanish','Blockchain','Programing','AI','Law','IOT','Android','Leadership','Business','Covid-19','Chemicals','Networking','python','Python','C','Mystifying','SQL','Algorithms','Computer']
for i in courses:    
    d_courses_list=df_org[df_org['course_title'].str.contains(i)]
    d_courses_list['Course_name'] = i
    data_courses=pd.concat([data_courses,d_courses_list],axis=0)

data_courses.shape

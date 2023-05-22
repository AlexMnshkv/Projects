#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Считываем данные
dataFedorov_0312 = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_4/dataFedorov.csv')
dataKPetrov_0312 =pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_4/dataKPetrov.csv')
dataPetrov_0312 =pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_4/dataPetrov.csv')
dataSmirnov_0312 =pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_4/dataSmirnov.csv')
dataVIvanov_0312 =pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_4/dataVIvanov.csv')
dataVPetrov_0312 =pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_4/dataVPetrov.csv')
dataFedorov_0312


# In[3]:


df = dataFedorov_0312
a = pd.Series()
path = ('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/')
path = path.split('/')
path = path[-2]
for i in df:
    df['data'] = path
    print(df)


# In[18]:


dataFedorov_0312['Name'] = ['Петр Федоров','Петр Федоров','Петр Федоров' ]
dataFedorov_0312['Date'] = []


# In[19]:


dataFedorov_0312


# In[65]:


df.groupby('quantity').agg({'quantity':sum})


# In[67]:


df.quantity.sum()


# In[8]:


df.head(10)


# In[34]:


df.head(10)


# In[5]:


#Собираем данные из папки data в один датафрейм
data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data')
df = pd.DataFrame()
# for i in data:
for j in data:
    data =os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j)
#       print(data)
    for  x in data:
        data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x)
        for z in data: 
            data = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x+'/'+ z)
            data.reset_index(drop=True)
            df = df.append(data)
   


# In[6]:


df


# In[7]:


df.quantity.sum()


# In[8]:


from datetime import datetime
import numpy as np

data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data') 
df = pd.DataFrame()
pdat = pd.Series()
# path = '/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data'
for j in data:
    data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j)
    for  x in data:
        data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x)
        for z in data: 
            path = ('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x+'/'+ z)
            path = path.split('/')
            path = path[-2]
            data = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x+'/'+ z)
            df = df.append(data)
            for i in df:
                df['name']=pd.Series(path)
                
            data.reset_index(drop=True)
            print(df['name'])
#             path_d = pdat.append(path)
#             dat = pd.Series(path[-3])
#             nam = pd.Series(path[-2])
#             df['date'] = dat
#             df['name'] = nam
      
#             df = df.append(data)

                       
   


# In[9]:


df


# In[10]:


df.groupby('name').agg({'quantity': 'count'})


# In[11]:


df.tail(25)


# In[12]:


data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data') 
df = pd.DataFrame()
dfname=pd.DataFrame()
pdat = pd.Series()
# path = '/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data'
for j in data:
    data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j)
    for  x in data:
        data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x)
        for z in data: 
            path = ('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x+'/'+ z)
            path = path.split('/')
            path = path[-2]
#             for i in df:
#             df['name']=path
            data = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x+'/'+ z)
            data['name']=path
            df = df.append(data)
            data.reset_index(drop=True)
           
            
df            


# In[13]:


df.tail(10)


# In[14]:


# Выясним, какой пользователь купил больше всего товаров.
df.groupby('name').agg({'quantity': 'sum'}).sort_values('quantity', ascending=False)


# In[38]:


# df1 = df.groupby(['product_id','quantity'], as_index=False).agg({'quantity': sum}).rename(columns={'quantity': 'quantity_counts'})
# df1.query('product_id==56')
df1=df.groupby('product_id').agg({'quantity':'sum'}).rename(columns={'product_id': 'product_id_counts'}).reset_index()
df1


# In[39]:


# Найдем топ-10 товаров по числу проданных единиц за всё время и построим барплот 
import seaborn as sns
plt.figure(figsize=(20, 10))
sns.barplot(x="product_id", y="quantity", data=df1)


# In[ ]:





# In[40]:


data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data') 
df = pd.DataFrame()
dfname=pd.DataFrame()
pdat = pd.Series()
# path = '/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data'
for j in data:
    data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j)
    for  x in data:
        data = os.listdir('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x)
        for z in data: 
            path = ('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x+'/'+ z)
            path = path.split('/')
            path_name = path[-2]
            path_date = path[-3]
#             for i in df:
#             df['name']=path
            data = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4/data/'+ j+'/'+x+'/'+ z)
            data['name']=path_name
            data['date']=path_date
            df = df.append(data)
            data.reset_index(drop=True)
           
            
df            


# In[41]:


df2 = df.groupby('date').agg({'quantity': 'count'}).rename(columns={'quantity': 'quantity_counts'})
df2


# In[43]:


df2 = df.groupby('date', as_index = False).agg({'quantity': sum}).rename(columns={'quantity': 'quantity_counts'})
df2


# In[44]:


# Посмотрим на продажи по дням
import seaborn as sns
plt.figure(figsize=(20, 10))
sns.barplot(x="date", y="quantity_counts", data=df2)


# In[87]:


df3 = df.groupby(['product_id','date','name']).agg({'quantity': sum}).rename(columns={'quantity': 'quantity_counts'})


# In[45]:


df


# In[48]:


df_drop=df.drop_duplicates()
df_drop


# In[51]:


# Найдем сколько пользователей приобрели какой-либо товар повторно (более 1 раза)? 
df_drop.groupby(['date','product_id']).agg({'name':'nunique'}).sort_values('name', ascending=False)


# In[88]:


df3


# In[ ]:





# In[46]:


df4 = df.drop_duplicates(subset='name')
df4 = df.drop_duplicates(subset='product_id')
df4 = df.drop_duplicates(subset='date')
df4


# In[162]:


df5 = df4.groupby(['product_id','name']).agg({'date': 'count'})
df5


# In[176]:


r=df4.groupby(['name','product_id']).agg({'date':sum})

r


# In[174]:


r.query('product_id!=1')
r


# In[181]:


df4 = df.drop_duplicates(subset=['name','date','quantity'])
df4


# In[205]:


df5 = df4.groupby(['name','date','product_id']).agg({'quantity':'sum'})
df5


# In[209]:


df0 = df.drop_duplicates(subset=['name','date','quantity'])
df0


#!/usr/bin/env python
# coding: utf-8

# In[4]:


# минипроект на фильтрацию данных
import pandas as pd
# Считываем данные
df = pd.read_excel('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4_inn/inn.xls')
df
tdf = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/shared/homeworks/python_ds_miniprojects/4_inn/necessary_inn.txt', header = None,)


# In[5]:


tdf


# In[6]:


tdf.columns=['INN']
tdf1=tdf['INN'].tolist()
# tdf1=pd.Series(tdf.INN)
tdf1


# In[9]:


df


# In[28]:


# извлечем из таблицы записи с ИНН
df2=df.query('head_inn in @tdf1')
df2


# In[31]:


# Найдем сумму колонки income,RUB в отобранных данных
df2['income,RUB'].sum()


# In[37]:


df


# In[ ]:





# In[24]:


inn = df.reg_number
inn


# In[7]:


df


# In[5]:


reg_number1 = df['reg_number'].tolist()
reg_number1


# In[ ]:





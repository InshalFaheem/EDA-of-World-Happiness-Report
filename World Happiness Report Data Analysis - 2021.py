#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as  plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly
import plotly.graph_objects as go
import plotly.express as px


import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot

import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)


import warnings
warnings.filterwarnings("ignore")


# In[2]:


sns.set_style('darkgrid')
plt.rcParams['font.size'] = 16
plt.rcParams['figure.figsize'] = (12, 6)


# In[3]:


data = pd.read_csv(r"E:\Data Analysis project jupyter lab\EDA Data Analysis Project\World Happiness Data Analysis\world-happiness-report-2021.csv")


# In[4]:


data.head()


# In[5]:


data_columns = ['Country name', 'Regional indicator', 'Happiness score','Logged GDP per capita', 'Social support','Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']


# In[6]:


data = data[data_columns].copy()


# In[7]:


happy_df = data.rename(columns = {'Country name': 'country_name', 'Regional indicator': 'regional_indicator',  'Happiness score': 'happiness_score', 'Logged GDP per capita': 'logged_GDP_per_capita','Social support':'social_support', 'Healthy life expectancy':'healthy_life_expectancy','Freedom to make life choices':'freedom_to_make_life_choices', 'Generosity':'generosity', 'Perceptions of corruption':'perceptions_of_corruption'})


# In[8]:


happy_df.head()


# In[9]:


happy_df.isnull().sum()


# # Plot Between happiness and GDP

# In[10]:


plt.rcParams['figure.figsize'] = (15, 7)
plt.title('Plot Between happiness and GDP')
sns.scatterplot(x = happy_df.happiness_score, y=happy_df.logged_GDP_per_capita, hue= happy_df.regional_indicator, s =200 );

plt.legend(loc = 'upper left', fontsize = '10')
plt.xlabel('Happiness Score')
plt.ylabel('GDP per capita')


# # GDP in various Reigons

# In[11]:


gdp_reigon = happy_df.groupby('regional_indicator')['logged_GDP_per_capita'].sum()
gdp_reigon


# In[12]:


df = happy_df
df = df.groupby('regional_indicator')['logged_GDP_per_capita'].sum()
df = df.reset_index()
ax = df.iplot(x="regional_indicator", y="logged_GDP_per_capita", kind='barh',  title ='GDP by region', theme='polar',
                xTitle = 'Logged GDP per capita', yTitle='Reigon' )
plt.show()


# # Total Countries

# In[13]:


total_countary = happy_df.groupby('regional_indicator')['country_name'].count()
total_countary


# # Correlation of different factors on Happiness score

# In[14]:


cor = happy_df.corr(method='pearson')
f,ax = plt.subplots(figsize  = (12, 7))
sns.heatmap(cor, mask= np.zeros_like(cor, dtype = bool),
        cmap="Blues", ax=ax, square=True)


# # Corruption in different regions

# In[15]:


f, ax = plt.subplots(figsize=(20, 10))
sns.despine(f)
df = happy_df
df = df.groupby('regional_indicator')['perceptions_of_corruption'].mean()
df = df.reset_index()
sns.barplot(x='perceptions_of_corruption', y='regional_indicator', data=df, ci=None, palette='Set3')
ax.set_title("Preception of corruption in various reigons", fontsize=32)
ax.set_xlabel("Preception of corruption", fontsize = 24)
ax.set_ylabel("Regional Indicator", fontsize = 24)
for rect in ax.patches:
 ax.text (rect.get_width(), rect.get_y() + rect.get_height() / 2,"%.1f%%"% rect.get_width(), weight='bold' )


# # Life Expectency of TOP and Bottom 10 Happiest Countries

# In[16]:


top10 = happy_df.head(10)
bottom10 = happy_df.tail(10)
top10


# In[17]:


f, ax = plt.subplots(1,2, figsize=(20, 8))
sns.set(font_scale=2)

plt.tight_layout(pad = 2)
xlabels = top10.country_name
ax[0].set_title("Top 10 happiest country life expectancy")
ax[0].set_xticklabels(xlabels, rotation = 45, ha='right' )
sns.barplot(x=top10.country_name, y=top10.healthy_life_expectancy, data=happy_df, ax=ax[0], ci=None, palette='Set3')
ax[0].set_xlabel("Country Name")
ax[0].set_ylabel("Life Expectnacy")


xlabels = bottom10.country_name
ax[1].set_title("Bottom 10 happiest country life expectancy")
ax[1].set_xticklabels(xlabels, rotation = 45, ha='right')
sns.barplot(x=bottom10.country_name, y=bottom10.healthy_life_expectancy, data=happy_df, ax=ax[1], ci=None, palette='Set3')
ax[1].set_xlabel("Country Name")
ax[1].set_ylabel("Life Expectnacy")

plt.show()


# # Freedom to make life choices vs happiness score

# In[18]:


plt.rcParams['figure.figsize']=(15,7)
sns.scatterplot(x=happy_df.freedom_to_make_life_choices, y=happy_df.happiness_score, hue=happy_df.regional_indicator, s= 200)
plt.legend(loc = 'upper left', fontsize ='12' )
plt.xlabel('Freedom to make life choices')
plt.ylabel('Happiness Score')


# # Corruption vs Happiness score

# In[19]:


plt.rcParams['figure.figsize']=(15,7)
sns.scatterplot(x=happy_df.happiness_score, y=happy_df.perceptions_of_corruption, hue=happy_df.regional_indicator, s= 200)
plt.legend(loc = 'lower left', fontsize ='14' )
plt.xlabel('Happiness Score')
plt.ylabel('Corruption')


# In[ ]:





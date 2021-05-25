#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine
from sqlalchemy.dialects import registry
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import snowflake.connector 
from snowflake.connector.pandas_tools import pd_writer
import datetime as dt 
import seaborn as sns


# In[2]:



#a `magic code` that allows ploting of charts within the notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# Sets all rows to display
pd.options.display.max_rows = None

#Stops a false alarm chaining error
pd.options.mode.chained_assignment = None


# In[3]:


registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')

engine = create_engine(
    'snowflake://{user}:{password}@{account}/'.format(
  user ='shreyareddy',
password ='Shreya.98',
account ='naa96735.us-east-1',
    )
)
try:
    connection = engine.connect()
    results = connection.execute('select current_version()').fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()


# In[4]:


conn = snowflake.connector.connect(
              user='shreyareddy',
              password='Shreya.98',
              account='naa96735.us-east-1',
              warehouse='ETL',
              database='YAYLUNCH',
              schema='RAILS_PUBLIC',
             role ='ETL' )


# In[5]:


cur =conn.cursor()


# In[6]:


# Execute a statement that will generate a result set.
sql = "select * from customer_analysis"
cur.execute(sql)

# Fetch the result set from the cursor and deliver it as the Pandas DataFrame.
df = cur.fetchall()


# In[9]:


df


# In[11]:


df1 = pd.DataFrame( df, columns=['Student_id','Student Name','parent_id','Email','Grade','First_Lunch','First_trunc_date','Last Lunch','School Name','Pick_updates','Months_since_start','meal_price'])


# In[13]:


df1.head()


# In[15]:


def explore(x):
    divider = "*_*"
    print("\n {} \n".format((divider*20))) #creates a dvider between each method output breaking at each end.
    
    print("Dataframe Makeup \n") #title for output.
    
    x.info() # Explains what the data and values the data is madeup from.
    
    print("\n {} \n".format((divider*20))) #creates a dvider between each method output breaking at each end.
    
    print("Descriptive Statistics \n\n", x.describe().round(2)) #Gives a statstical breakdown of the data.
    
    print("\n {} \n".format((divider*20))) #creates a dvider between each method output breaking at each end.
    
    print("Shape of dataframe: {}".format(x.shape)) # Gives the shape of the data.
    
    print("\n {} \n".format((divider*20))) #creates a dvider between each method output breaking at each end.
    return


# In[16]:


explore(df1)


# In[17]:



def missing_data(x):
    return x.isna().sum()


# In[18]:



missing_data(df1)


# In[19]:



#drops missing data from the CustomerID column
cleaned_data = df1.dropna(subset=['parent_id'])


# In[20]:


explore(cleaned_data)


# In[21]:



cleaned_data.head()


# In[22]:



#Uses the datetime function to gets the month a datetime stamp and strips the time
def get_month(x):
    return dt.datetime(x.year, x.month, 1) #year, month, incremints of day


# In[23]:



#Create a new column 
cleaned_data['InvoiceMonth'] = cleaned_data['Pick_updates'].apply(get_month)


# In[24]:


#Always inspect the data you've just created
cleaned_data['InvoiceMonth']


# In[25]:



#Create a CohortMonth column by grouping data and selecting the earliest instance in the data. 
cleaned_data['CohortMonth'] = cleaned_data.groupby('parent_id')['InvoiceMonth'].transform('min')


# In[26]:


cleaned_data['CohortMonth']


# In[27]:



cleaned_data.head()


# In[28]:


#When passed a datetime column this functions splits out year, month, day

def get_date(df1, column):
    year = df1[column].dt.year
    month = df1[column].dt.month
    day = df1[column].dt.day
    return year, month, day


# In[29]:


#splits invoiced month and data into single variables
invoice_year, invoice_month, _ = get_date(cleaned_data, 'InvoiceMonth')


# In[30]:


#Inspect the variable
invoice_month[:30] #[:30] selects the first 30 rows of data


# In[31]:



#Inspect the variable
invoice_year[:30] #[:30] selects the first 30 rows of data


# In[32]:


#splits cohort month and data into single variables
cohort_year, cohort_month, _ = get_date(cleaned_data, 'CohortMonth')


# In[33]:



cohort_month[:30]


# In[34]:


cohort_year[:30]


# In[35]:


# Creating a variable which holds the differnce between the invoice and cohort year 
year_diff = invoice_year - cohort_year


# In[36]:


year_diff


# In[37]:


# Creating a variable which holds the differnce between the invoice and cohort month 
month_diff = invoice_month - cohort_month


# In[38]:


month_diff


# In[39]:


#Now creating a column that has the calclation shows the 
cleaned_data['CohortIndex'] = year_diff * 12 + month_diff + 1


# In[40]:


cleaned_data['CohortIndex']


# In[41]:


cleaned_data.head()


# In[42]:


#Group the data by columns CohortMonth','CohortIndex' then aggreate by column 'CustomerID'
cohort_data = cleaned_data.groupby(
    ['CohortMonth', 'CohortIndex'])['parent_id'].apply(pd.Series.nunique).reset_index()


# In[43]:



#Take the cohort_data and plumb it into a Pivot Table. Setting index, columns and values as below.
cohort_count = cohort_data.pivot_table(index = 'CohortMonth',
                                       columns = 'CohortIndex',
                                       values = 'parent_id')


# In[44]:


cohort_count


# In[45]:


cohort_size = cohort_count.iloc[:,0] #select all the rows : select the first column
retention = cohort_count.divide(cohort_size, axis=0) #Divide the cohort by the first column
retention.round(3) # round the retention to 3 places


# In[46]:


plt.figure(figsize = (30,30))
plt.title('Cohort Analysis - Retention Rate')
sns.heatmap(data = retention, 
            annot = True, 
            fmt = '.0%', 
            vmin = 0.0,
            vmax = 0.5,
            cmap = "YlGnBu")
plt.show()


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np


# In[20]:


#pip install beautifulsoup4
#pip install pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
#nltk.download('punkt')
nltk.download
import collections
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize, sent_tokenize    
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords


# In[21]:


data = pd.read_excel(r'C:\Users\shrey\Desktop\fall 2021 survey.xlsx')


# In[22]:


data


# In[5]:


#data['tokens'] =data['Other vendors'].apply(nltk.word_tokenize)
#data['tokens']
data


# In[ ]:





# In[ ]:





# In[6]:


data


# In[ ]:





# In[7]:



def RemovePunc(txt):
    punc = '''!()-[]–{};:"“”\,. <>/?@#$%^&*_~'''
    for ele in txt:
        if ele in punc:
            txt = txt.replace(ele, " ")
    return txt


# In[8]:


txt = RemovePunc(data['Other vendors'])


# In[9]:


txt


# In[10]:


stopwords_data =stopwords.words('english')
stopwords_data


# In[ ]:





# In[11]:



 # removing stop words from wordList
stopwords_data = [p for p in txt if p not in stopwords.words('english')]

print(len(stopwords_data))
print(stopwords_data)


# In[12]:


#2.3 Lemmatize the words
lemmatizer = WordNetLemmatizer() 

LemmetizedWords = list()
for i in stopwords_data:
    temp = lemmatizer.lemmatize(i)
    LemmetizedWords.append(temp)

data1 = list()
for i in LemmetizedWords:
    if len(i)> 1:
        data1.append(i)
print(len(data1))
print(data1)


# In[13]:



freq_dist = nltk.FreqDist(data1)
print(freq_dist)
freq_dist.plot()
print(freq_dist.most_common(15))
freq_dist.plot(15)


# In[14]:


df = freq_dist.most_common(100)


# In[15]:


print(df)
freq_dist.plot(20)


# In[16]:


df1 = pd.DataFrame( df, columns= ['Vendors','Frequency'])
df1


# In[17]:


new = pd.ExcelWriter('Vendors_list.xlsx')
# write dataframe to excel
df1.to_excel(new)
# save the excel
new.save()


# In[18]:


wordcloud = WordCloud(width = 1000, height = 500).generate(" ".join(df1))
wordcloud


# In[ ]:


text = " ".join(review for review in df1.Vendors)
print ("There are {} words in the combination of all review.".format(len(text)))


# In[ ]:



# Generate a word cloud image
wordcloud = WordCloud(width=2000, height=1000,max_font_size=500, max_words=200,background_color="white").generate(text)
plt.figure( figsize=(20,10) )
# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[ ]:



# wordcloud function

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color = 'white',
        max_words = 400,
        max_font_size = 40, 
        scale = 3,
        random_state = 42
    ).generate(str(data))

    fig = plt.figure(1, figsize = (20, 20))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize = 20)
        fig.subplots_adjust(top = 2.3)

    plt.imshow(wordcloud)
    plt.show()
    
# print wordcloud
show_wordcloud(df1["Vendors"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





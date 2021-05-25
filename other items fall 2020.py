#!/usr/bin/env python
# coding: utf-8

# In[67]:


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
from nltk.corpus import wordnet
import string
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


# In[68]:


new = pd.read_excel(r'C:\Users\shrey\Desktop\Other items.xlsx')
new


# In[69]:


new1= new.dropna()
new1


# In[70]:



def RemoveNone(txt):
    punc = 'No,no,N/A,na,None, N/a,na,Na,''()-[]–{};:"“”\,. <>/?@#$%^&*_~' ''''''
    for ele in txt:
        if ele in punc:
            txt = txt.replace(ele, " ")
    return txt


# In[71]:


txt = RemoveNone(new1['Other Items'])
txt


# In[72]:



# Python program to convert a list to string
    
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = '' 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
        


# In[73]:


string=listToString(txt)
string


# In[74]:


txt1 = word_tokenize(string)
for i in string:
    wordsList = nltk.word_tokenize(i)
    
txt1


# In[75]:


stopwords_data = [p for p in txt1 if p not in stopwords.words('english')]

print(len(stopwords_data))
print(stopwords_data)






# In[76]:


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


# In[77]:


#2.4 Word distribution using Frequency distribution
#2.5 Plot for top 15 words

freq_dist = nltk.FreqDist(data1)
print(freq_dist)
freq_dist.plot()
print(freq_dist.most_common(15))
freq_dist.plot(15)


# In[78]:


frequency_items = freq_dist.most_common(100)
data_frequency = pd.DataFrame(frequency_items, columns=['Items','Frequency'])
data_frequency


# In[79]:


new5 = pd.ExcelWriter('Items_List.xlsx')
# write dataframe to excel
data_frequency.to_excel(new5)
# save the excel
new5.save()


# In[80]:


#3. Summarize the text

#3.1 Word Weight frequency

wordweight = {}

for i in data1:
        if i not in wordweight.keys():
            wordweight[i] = 1
        else:
            wordweight[i] += 1
            
wordfreq = max(wordweight.values()) # It retreves the max weight of the most frequent word

# Word weighted frequency is calculated for each word
for key in wordweight.keys():
    wordweight[key] = wordweight[key]/wordfreq
print(wordweight)


# In[81]:



# wordcloud function

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color = 'white',
        max_words = 200,
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
show_wordcloud(data1)


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





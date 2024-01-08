#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install requests


# In[2]:


pip install bs4


# In[2]:


from bs4 import BeautifulSoup as bs
import requests,openpyxl


# In[3]:


excel = openpyxl.Workbook()#it creats a xl sheet
sheet=excel.active#gets the sheet active
sheet.title='Top Movies of 2023'
print(excel.sheetnames)
sheet.append(['S.no','Movie','Rating'])#loading column names


# In[4]:


url = "https://www.imdb.com/list/ls576754431/"#getting the url


# In[5]:


source = requests.get(url)#requesting & it give the status of the code 
source


# In[6]:


soup = bs(source.text,'html.parser')#using html parser
soup


# In[7]:


movies = soup.find_all('div', class_='lister-item mode-detail')


# In[8]:


print(len(movies))


# In[9]:


for movie in movies:
    name = movie.find('h3', class_="lister-item-header").a.text
    rank = movie.find('h3', class_="lister-item-header").span.text
    rate = movie.find('div', class_="ipl-rating-widget").find('div', class_="ipl-rating-star small").find('span', class_="ipl-rating-star__rating").text
    print(rank,end=" ")
    print(name,end=" ")
    print(rate)
    sheet.append([rank,name,rate])
    
excel.save('Top Movies of 2023.xlsx')


# In[ ]:





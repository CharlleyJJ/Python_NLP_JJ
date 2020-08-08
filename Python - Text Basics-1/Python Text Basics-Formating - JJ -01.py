#!/usr/bin/env python
# coding: utf-8

# In[1]:


person = "Jose"


# In[2]:


print(f"my name is {person}")


# In[9]:


d = {'a':123, 'b':456}


# In[13]:


mylist = [0,23,2]


# In[14]:


print(f"my number is {mylist[1]}")


# In[18]:


library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting---------GG', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]


# In[19]:


library


# In[31]:


for author, topic, pages in library:
    print(f"{author:{10}} {topic:{30}} {pages:.>{10}}")


# In[32]:


from datetime import datetime


# In[33]:


today = datetime(year=2020,month=8,day=8)


# In[36]:


print(f"{today: %B %d, %Y}")


# In[37]:


today


# In[ ]:





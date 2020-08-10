#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'test.txt', 'Hello testing text file creation\nSecond line of the text file.\nThis method just works in Jupyter IDE ...')


# In[3]:


#myfile = open("Whoops.txt") - Error N°2 it means wrong path or the file doesn't exist.


# In[5]:


pwd ## This command shows which directory we actually are working with ( and so do your created file should be).


# In[6]:


myfile = open("test.txt")


# In[7]:


myfile ##<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'> if show something like this it means that the file is stored in the variable


# In[8]:


myfile.read()


# In[9]:


myfile.read()


# In[10]:


myfile.seek(0)


# In[11]:


myfile.read()


# In[12]:


myfile.seek(0)


# In[13]:


content = myfile.read()


# In[14]:


print(content)


# In[15]:


content


# In[16]:


myfile.close()


# In[17]:


myfile = open('test.txt')


# In[18]:


myfile.readlines()


# In[19]:


myfile.seek(0)


# In[20]:


mylines = myfile.readlines()


# In[21]:


mylines


# In[22]:


for line in mylines:
    print(line[0])


# In[23]:


for line in mylines:
    print(line.split()[0])


# In[24]:


myfile = open('test.txt','w+')


# In[26]:


myfile.read()


# In[27]:


myfile.write('My brand new text')


# In[28]:


myfile.seek(0)


# In[29]:


myfile.read()


# In[30]:


## w+ overwrite the whole file


# In[31]:


myfile.close()


# In[32]:


##Append method, keep the old information inside the file


# In[33]:


myfile=open("whoops.txt",'a+') ##this will create the file and not show any error


# In[34]:


myfile.write("My first Line in A+ Opening")


# In[36]:


myfile.close()


# In[37]:


newfile = open('whoops.txt')


# In[38]:


newfile.read()


# In[39]:


newfile.write('Trying to write something with only read permissions')


# In[40]:


newfile.close()


# In[41]:


myfile=open('whoops.txt', mode='a+')


# In[42]:


myfile.write('This is an Added Line because I used a+ mode')


# In[43]:


myfile.seek(0)


# In[45]:


myfile.read()


# In[46]:


myfile.write('This is a real new line, on the next line')


# In[47]:


myfile.seek(0)


# In[48]:


myfile.read()


# In[49]:


myfile.seek(0)


# In[50]:


print(myfile.read())


# In[54]:


## Automatic closing line - context manager "with" auto close the files


# In[52]:


with open('whoops.txt', 'r') as mynewfile:
    myvariable = mynewfile.readlines()


# In[53]:


myvariable


# In[ ]:





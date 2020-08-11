#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = "The phone number of the agent is 408-555-1234. Call soon! "


# In[2]:


"phone" in text


# In[3]:


"408-555-1234" in text


# In[4]:


import re ## Regular Expression Library


# In[5]:


pattern = "phone"


# In[6]:


re.search(pattern,text)


# In[7]:


my_match = re.search(pattern,text)


# In[8]:


my_match.span() ## Representa o index de minha string dizendo que a palavra "phone" está alocada na posição 4 e se encerra na 9 da string inicial.


# In[9]:


my_match.start()


# In[10]:


my_match.end()


# In[11]:


text = "My phone is a new phone"


# In[12]:


match = re.search(pattern,text) ## este método irá descobrir somente a primeira instância do que estamos procurando


# In[13]:


match.span()


# In[14]:


## Para verificar todas as ocorrências segue o método.


# In[15]:


all_matches = re.findall("phone",text)


# In[16]:


len(all_matches)


# In[17]:


for match in re.finditer("phone",text):
    print (match.span())
match.group()  


# In[18]:


## Pesquisa de padrões generalizados


# In[19]:


text


# In[20]:


NewText = "My phone number is 62 99111-0000"


# In[21]:


NewText


# In[22]:


pattern = r'\d\d\s\d\d\d\d\d-\d\d\d\d'


# In[23]:


phone_number = re.search(pattern,NewText)


# In[24]:


phone_number


# In[25]:


phone_number.group()


# In[77]:


NewText2 = "New phone 62 99999-1234 and older phone 62 99947-1235 010.183.381-43"


# In[78]:


New_phone = re.findall(pattern,NewText2)


# In[79]:


New_phone


# In[80]:


## Tentando verificar um cpf -


# In[81]:


CPFpattern = r"\d{3}.\d{3}.\d{3}-\d{2}"


# In[97]:


CPFfinder = re.search(CPFpattern,NewText2)


# In[101]:


CPFfinder.group()


# In[99]:


mymatch = CPFfinder


# In[104]:


mymatch


# Identifiers for Characters in Patterns

# <table ><tr><th>Character</th><th>Description</th><th>Example Pattern Code</th><th >Exammple Match</th></tr>
# 
# <tr ><td><span >\d</span></td><td>A digit</td><td>file_\d\d</td><td>file_25</td></tr>
# 
# <tr ><td><span >\w</span></td><td>Alphanumeric</td><td>\w-\w\w\w</td><td>A-b_1</td></tr>
# 
# 
# 
# <tr ><td><span >\s</span></td><td>White space</td><td>a\sb\sc</td><td>a b c</td></tr>
# 
# 
# 
# <tr ><td><span >\D</span></td><td>A non digit</td><td>\D\D\D</td><td>ABC</td></tr>
# 
# <tr ><td><span >\W</span></td><td>Non-alphanumeric</td><td>\W\W\W\W\W</td><td>*-+=)</td></tr>
# 
# <tr ><td><span >\S</span></td><td>Non-whitespace</td><td>\S\S\S\S</td><td>Yoyo</td></tr></table>

# And <b>Quantifiers</b>

# <table ><tr><th>Character</th><th>Description</th><th>Example Pattern Code</th><th >Exammple Match</th></tr>
# 
# <tr ><td><span >+</span></td><td>Occurs one or more times</td><td>	Version \w-\w+</td><td>Version A-b1_1</td></tr>
# 
# <tr ><td><span >{3}</span></td><td>Occurs exactly 3 times</td><td>\D{3}</td><td>abc</td></tr>
# 
# 
# 
# <tr ><td><span >{2,4}</span></td><td>Occurs 2 to 4 times</td><td>\d{2,4}</td><td>123</td></tr>
# 
# 
# 
# <tr ><td><span >{3,}</span></td><td>Occurs 3 or more</td><td>\w{3,}</td><td>anycharacters</td></tr>
# 
# <tr ><td><span >\*</span></td><td>Occurs zero or more times</td><td>A\*B\*C*</td><td>AAACC</td></tr>
# 
# <tr ><td><span >?</span></td><td>Once or none</td><td>plurals?</td><td>plural</td></tr></table>

# In[ ]:





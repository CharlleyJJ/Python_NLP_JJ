#!/usr/bin/env python
# coding: utf-8

# In[2]:


text = "The phone number of the agent is 408-555-1234. Call soon! "


# In[3]:


"phone" in text


# In[4]:


"408-555-1234" in text


# In[5]:


import re ## Regular Expression Library


# In[6]:


pattern = "phone"


# In[7]:


re.search(pattern,text)


# In[8]:


my_match = re.search(pattern,text)


# In[9]:


my_match.span() ## Representa o index de minha string dizendo que a palavra "phone" está alocada na posição 4 e se encerra na 9 da string inicial.


# In[10]:


my_match.start()


# In[11]:


my_match.end()


# In[12]:


text = "My phone is a new phone"


# In[13]:


match = re.search(pattern,text) ## este método irá descobrir somente a primeira instância do que estamos procurando


# In[14]:


match.span()


# In[15]:


## Para verificar todas as ocorrências segue o método.


# In[16]:


all_matches = re.findall("phone",text)


# In[17]:


len(all_matches)


# In[18]:


for match in re.finditer("phone",text):
    print (match.span())
match.group()  


# In[19]:


## Pesquisa de padrões generalizados


# In[20]:


text


# In[21]:


NewText = "My phone number is 62 99111-0000"


# In[22]:


NewText


# In[23]:


pattern = r'\d\d\s\d\d\d\d\d-\d\d\d\d'


# In[24]:


phone_number = re.search(pattern,NewText)


# In[25]:


phone_number


# In[26]:


phone_number.group()


# In[27]:


NewText2 = "New phone 62 99999-1234 and older phone 62 99947-1235 010.183.381-43"


# In[28]:


New_phone = re.findall(pattern,NewText2)


# In[29]:


New_phone


# In[30]:


## Tentando verificar um cpf -


# In[38]:


CPFpattern = r"\d{3}.\d{3}.\d{3}-\d{2}" ## If you are looking for just a part of the pattern, you can slice it with ( \d{3}  ) for example and then by changing the index on the .group(n) it will show you a sliced part of the expression.


# In[39]:


CPFfinder = re.search(CPFpattern,NewText2)


# In[40]:


CPFfinder.group()


# In[41]:


mymatch = CPFfinder


# In[42]:


mymatch


# In[43]:


mymatch.group()


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

# In[44]:


##PART-2


# In[45]:


re.search(r"man|woman"," This woman was here")


# In[54]:


re.findall(r".at","The cat in the hat sat at my lap and splat around") ## the dot is a wildcard in the search query


# In[60]:


re.findall(r"\d$","This ends with 2")


# In[61]:


re.findall(r"^\d","1 is the number one")


# In[62]:


phrase = "there are 3 numbers inside this sentence 34 and 77"


# In[63]:


re.findall(r"[^\d]",phrase)


# In[64]:


re.findall(r"[^\d]+",phrase) ## signs  reajust the phrase


# In[65]:


test_phrase = "this is a string but it has punctuation. How to remove it all ?"


# In[71]:


re.findall(r"[^\W]+", test_phrase) ## removes everything , but you can filter the exclusion


# In[86]:


mylist = re.findall(r"[^!.? ]+", test_phrase) ## so here if you don't type space inside the brackets it won't exclude it


# In[87]:


mylist


# In[88]:


## if you want to restore these lost spaces, just create a join method


# In[93]:


' '.join(mylist)


# In[94]:


text = "Only find the hyphen-words. where is the long-ish dash word?"


# In[96]:


re.findall(r"[\w]+-[\w]+",text)


# In[ ]:





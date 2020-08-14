#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Python Text Basics Assessment
# 
# Welcome to your assessment! Complete the tasks described in bold below by typing the relevant code in the cells.<br>
# You can compare your answers to the Solutions notebook provided in this folder.

# ## f-Strings
# #### 1. Print an f-string that displays `NLP stands for Natural Language Processing` using the variables provided.

# In[3]:


abbr = 'NLP'
full_text = 'Natural Language Processing'

# Enter your code here:
standard= " stands for "
abbr+standard+full_text


# In[8]:


##Dictionary = [(abbr),(full_text)]
##Dictionary


# In[9]:


print(f"{abbr} stands for {full_text}")


# ## Files
# #### 2. Create a file in the current working directory called `contacts.txt` by running the cell below:

# In[195]:


get_ipython().run_cell_magic('writefile', 'contacts.txt', 'First_Name Last_Name, Title, Extension, Email')


# #### 3. Open the file and use .read() to save the contents of the file to a string called `fields`.  Make sure the file is closed at the end.

# In[14]:


pwd


# In[116]:


# Write your code here:
myfile = open('contacts.txt')



    
# Run fields to see the contents of contacts.txt:
fields = myfile.read()
print(fields)

# Fechando o arquivo
myfile.close()


# ## Working with PDF Files
# #### 4. Use PyPDF2 to open the file `Business_Proposal.pdf`. Extract the text of page 2.

# In[132]:


# Perform import
import PyPDF2

# Open the file as a binary object
Myfile2 = open('Business_Proposal.pdf', mode='rb')

# Use PyPDF2 to read the text of the file
PDF_reader = PyPDF2.PdfFileReader(Myfile2)
PDF_reader.numPages


# Get the text from page 2 (CHALLENGE: Do this in one step!)
page_two_text = PDF_reader.getPage(1)
Pg2=page_two_text.extractText()




# Close the file
Myfile2.close()

# Print the contents of page_two_text
print(Pg2)


# #### 5. Open the file `contacts.txt` in append mode. Add the text of page 2 from above to `contacts.txt`.
# 
# #### CHALLENGE: See if you can remove the word "AUTHORS:"

# In[190]:


import re
Myfile3 = open("contacts.txt",mode="a+")


# In[191]:


Myfile3.write(f"{Pg2}")


# In[192]:


Myfile3.seek(0)
My3 = print(Myfile3.read())
print(My3)


# In[197]:


# CHALLENGE Solution (re-run the %%writefile cell above to obtain an unmodified contacts.txt file):
with open("contacts.txt", "a+") as f:
    f.write(Pg2[8:])
    f.seek(0)
    print(f.read())



# ## Regular Expressions
# #### 6. Using the `page_two_text` variable created above, extract any email addresses that were contained in the file `Business_Proposal.pdf`.

# In[208]:


import re

# Enter your regex pattern here. This may take several tries!
pattern = ("[\w]+@+[\w]+.[\w]+")

print(Pg2)
print(pattern)

email_list = re.findall(pattern,Pg2)
print(email_list)


# ### Great job!

# In[ ]:





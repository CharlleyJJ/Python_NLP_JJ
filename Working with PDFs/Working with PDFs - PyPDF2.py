#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2


# In[2]:


myfile = open('US_Declaration.pdf', mode='rb') ##reading binary method - used for pdfs


# In[3]:


pdf_reader = PyPDF2.PdfFileReader(myfile)


# In[4]:


pdf_reader.numPages


# In[5]:


page_one= pdf_reader.getPage(0)


# In[7]:


page_one.extractText()


# In[8]:


print(page_one.extractText())


# In[9]:


mytext = page_one.extractText()


# In[10]:


myfile.close()


# In[11]:


f = open('US_Declaration.pdf','rb')


# In[12]:


pdf_reader = PyPDF2.PdfFileReader(f)


# In[13]:


first_page = pdf_reader.getPage(0)


# In[14]:


pdf_writer = PyPDF2.PdfFileWriter()


# In[15]:


pdf_writer.addPage(first_page)


# In[17]:


pdf_output = open('Meu_novo_PDF.pdf','wb')


# In[18]:


pdf_writer.write(pdf_output)


# In[19]:


pdf_output.close()


# In[20]:


f.close()


# In[ ]:





# In[ ]:





# In[21]:


Meu_novo = open('Meu_novo_PDF.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(Meu_novo)


# In[22]:


pdf_reader.numPages


# In[26]:


f = open('US_Declaration.pdf', 'rb')

pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    
    page = pdf_reader.getPage(p)
    
    pdf_text.append(page.extractText())
    
f.close()


# In[28]:


len(pdf_text)


# In[29]:


for page in pdf_text:
    print(page)
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')


# In[ ]:





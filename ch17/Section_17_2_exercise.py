#!/usr/bin/env python
# coding: utf-8

# In[28]:


"""
Description: This program simulates the exercise given at page 730 of Intro to Python for Computer Science and Data Science book.
It will perform basic commands on how to perform the CRUD operations with a database using sqlite3.

Section 17.2 Chapter 17 Big Data (page 730-741)

Name: Andrea Marcelli
"""


import sqlite3


# Creating a connection with the database
connection = sqlite3.connect('books.db')


# In[29]:


import pandas as pd


# Using SQL statements to retrieved DataFrame content
pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])


# In[30]:


# Display the titles table's content
pd.read_sql('SELECT * FROM titles', connection)


# In[31]:


# Storing in a variable the DataFrame returned values requested with an SQL statement
df = pd.read_sql('SELECT * FROM author_ISBN', connection)


# Display top 5 elements
df.head()


# In[32]:


# Displaying first and last columns of authors table
pd.read_sql('SELECT first, last FROM authors', connection)


# In[33]:


# Delimiting and retrieving SQL selection criteria. Title Edition Copyright > 2016
pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection)


# In[34]:


# Display all authors whose last name starts with letter D
pd.read_sql("""SELECT id, first, last FROM authors WHERE last LIKE 'D%'""", connection, index_col=['id'])


# In[35]:


# Displaying all authors whose last name start with any character followed by the letter b
pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", connection, index_col=['id'])


# In[36]:


# Sorting titles in ascending order
pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)


# In[37]:


# Sorting authors' names by last name, then by first name for any authors who have the same last name
pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last, first""", connection, index_col=['id'])


# In[38]:


# Sorting the authors in descending order by last name and ascending order by first name for any authors who have the same last name
pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last DESC, first ASC""", connection, index_col=['id'])


# In[39]:


# Display isbn, title, edition and copyright of each boko in titles table with a title ending with 'How to Program'
pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title""", connection)


# In[40]:


# Display a list of authors with their isbn book
pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first""", connection).head()


# In[41]:


# Adding a cursor to execute SQL statements that modify the database
cursor = connection.cursor()

# Inserting a ROW inside a table
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")


# In[42]:


pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[43]:


# Modifying an existing value
cursor = cursor.execute("""UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue'""")


# In[44]:


# Check number of rows that were modified
cursor.rowcount


# In[45]:


# Check if the UPDATE of an existing value was made with success
pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[20]:


# Removing rows from a table
cursor = cursor.execute('DELETE FROM authors WHERE id=6')

cursor.rowcount


# In[21]:


pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[46]:


pd.read_sql("""SELECT title, edition FROM titles ORDER BY edition DESC""", connection).head(3)


# In[47]:


pd.read_sql("""SELECT * FROM authors WHERE first LIKE 'A%'""", connection)


# In[48]:


pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title NOT LIKE '%How to Program' ORDER BY title""", connection)


# In[49]:


# When we finished our taks, close the connection with the database :)
connection.close()


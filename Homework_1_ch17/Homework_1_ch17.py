#!/usr/bin/env python
# coding: utf-8

# In[17]:


"""
Description: This program will use the operations learned from Section 17.2 of the book, CRUD operation
(Check README.md of the repository or the ch17 folder for the exercise example using sqlite).
The folliwing are the tasks required by the exercise 17.1 at page 799 of Chapter 17:

    a) Select all authors last names from the authors table in descending order.
    b) Select all book titles from titles table in ascending order.
    c) Use an INNER JOIN to select all the books for a specific author. Include the title, copyright year and ISBN.
    Order the information alphabetically by title.
    d) Insert a new author into the authors table.
    e) Insert a new title fro an author. Remember taht the book must have an entry i the author_ISBN table
    and an entry in the titles table.

Name: Andrea Marcelli
"""


import pandas as pd
import sqlite3

# Connecting to the database
connection = sqlite3.connect('books.db')


# In[34]:


# pd.options.display.max_columns = 10
# Select all authors last names from the authors table in descending order (a.)
pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection)


# In[35]:


# Select all book titles from titles table in ascending order (b.)
pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)


# In[21]:


# Use an INNER JOIN to select all the books for a specific author. Include the title, copyright year and ISBN.
# Order the information alphabetically by title. (c.)
pd.read_sql("""SELECT titles.title, titles.copyright, author_ISBN.isbn FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn INNER JOIN authors ON author_ISBN.id = authors.id WHERE authors.last = 'Deitel' ORDER BY titles.title ASC""", connection)


# In[36]:


# Insert a new author into the authors table (d.)
# To do so we will need a cursor, which using the cursor method gives us the possibility to modify the database
cursor = connection.cursor()


# In[37]:


# Now we can insert a new author inside the authors table
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Master', 'OTW')""")


# In[51]:


# Let's check quickly if it worked
pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[52]:


# Nice, it worked! Now let's continue with the last step

# Insert a new title for an author.
# Remember taht the book must have an entry i the author_ISBN table and an entry in the titles table. (e.)
cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright) VALUES ('1711729299', 'Getting Started Becoming a Master Hacker', 1, 2019)""")


# In[55]:


# Once create the content for the titles table we will add the content for the author_ISBN table.
# After we will have all three tables updated with the new author first and last name as well as his/her book information
cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES (6, "1711729299")""")


# In[57]:


# Let's check quickly if it worked
pd.read_sql("""SELECT titles.title, titles.copyright, author_ISBN.isbn FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn INNER JOIN authors ON author_ISBN.id = authors.id WHERE authors.first = 'Master'""", connection)


# In[58]:


"""
Great it worked!

If there is need to delete something, using this expression might help
- cursor = cursor.execute('DELETE FROM titles WHERE isbn=1711729299') - Change the arguments with your needs

Thank you for practicing with me using Big Data, see you soon!
"""


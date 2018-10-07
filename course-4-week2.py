# Relational Databases
# Terminologies
# Database - contains many tables​
# Relation (or table) - contains tuples and attributes​
# Tuple (or row) - a set of fields that generally represents an “object” like a person or a music track​
# Attribute (also column or field) - one of possibly many elements of data corresponding to the object represented by the row​

# A relation is defined as a set of tuples that have the same attributes.   A tuple usually represents an object and information about that object.  Objects are typically physical objects or concepts.   A relation is usually described as a table, which is organized into rows and columns.   All the data referenced by an attribute are in the same domain and conform to the same constraints. 

# Structured Querying Language(SQL)
# Structured Query Language is the language we use to issue commands to the database​
# -  Create data (a.k.a Insert)​
# -  Retrieve data​
# -  Update data​
# -  Delete data 

# Web Applications w/ Databases​
# Application Developer - Builds the logic for the application, the look and feel of the application - monitors the application for problems​
# Database Administrator - Monitors and adjusts the database as the program runs in production​
# Often both people participate in the building of the “Data model”​

# Datbase model
# A database model or database schema is the structure or format of a database, described in a formal language supported by the database management system. In other words, a “database model” is the application of a data model when used in conjunction with a database management system.​

# Create first table:
# CREATE TABLE `Users` (
#  name VARCHAR(128),
#  email VARCHAR(128)
# );

# Insert into table SQL Query - The Insert statement inserts a row into the table
# INSERT INTO `Users`(`name`,`email`) VALUES ('NULL','NULL');

# Delete from Table using SQL Query
# DELETE FROM Users WHERE email="anand@andy.com"

# Update
# UPDATE Users SET name='Anand' WHERE email="abc@abc.edu"

# Read
# SELECT * FROM Users WHERE email="abc@abc.edu"

# Order By or Sort the Database fields
# SELECT * FROM Users ORDER BY name

# SQL Summary of commands
# INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')​
# DELETE FROM Users WHERE email="anand@andy.com"
# UPDATE Users SET name='Anand' WHERE email="abc@abc.edu"
# SELECT * FROM Users
# SELECT * FROM Users WHERE email="abc@abc.edu"
# SELECT * FROM Users ORDER BY name


# Creating DB using Python

# import sqlite3

# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('''
# CREATE TABLE Counts (email TEXT, count INTEGER)''')

# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (email, count)
#                 VALUES (?, 1)''', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
#                     (email,))
#     conn.commit()

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.close()

# Twitter Spider Python script
# from urllib.request import urlopen
# import urllib.error
# import twurl
# import json
# import sqlite3
# import ssl

# TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# conn = sqlite3.connect('spider.sqlite')
# cur = conn.cursor()

# cur.execute('''
#             CREATE TABLE IF NOT EXISTS Twitter
#             (name TEXT, retrieved INTEGER, friends INTEGER)''')

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     acct = input('Enter a Twitter account, or quit: ')
#     if (acct == 'quit'): break
#     if (len(acct) < 1):
#         cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
#         try:
#             acct = cur.fetchone()[0]
#         except:
#             print('No unretrieved Twitter accounts found')
#             continue

#     url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
#     print('Retrieving', url)
#     connection = urlopen(url, context=ctx)
#     data = connection.read().decode()
#     headers = dict(connection.getheaders())

#     print('Remaining', headers['x-rate-limit-remaining'])
#     js = json.loads(data)
#     # Debugging
#     # print json.dumps(js, indent=4)

#     cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))

#     countnew = 0
#     countold = 0
#     for u in js['users']:
#         friend = u['screen_name']
#         print(friend)
#         cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
#                     (friend, ))
#         try:
#             count = cur.fetchone()[0]
#             cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
#                         (count+1, friend))
#             countold = countold + 1
#         except:
#             cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
#                         VALUES (?, 0, 1)''', (friend, ))
#             countnew = countnew + 1
#     print('New accounts=', countnew, ' revisited=', countold)
#     conn.commit()

# cur.close()




# Assessment - Counting Organizations - WIP
# Fixed from here:
# https://github.com/joanake/python/tree/master/coursera-4


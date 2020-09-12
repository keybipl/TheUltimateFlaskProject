import sqlite3

db = sqlite3.connect('terminarz.db')
cursor = db.cursor()

cursor.execute('''data.db''')
# cursor.execute('''INSERT INTO Users (name, location) values ('Anthony', 'Texas')''')

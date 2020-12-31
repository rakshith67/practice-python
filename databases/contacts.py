import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES('rakshith', 123456, '@email.com')")
db.execute("INSERT INTO contacts VALUES('Brain', 1233576, 'a@email.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
print(cursor.fetchone())
print(cursor.fetchmany(2))
print(cursor.fetchall())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 40)

db.commit()
db.close()

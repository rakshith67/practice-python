import sqlite3

db = sqlite3.connect("contacts.sqlite")

phone_number = input("Please enter your number ")
new_email = "updated@email.com"
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone_number))
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(email)
    print(phone)
    print("-" * 40)

db.close()

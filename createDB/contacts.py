import sqlite3


db = sqlite3.connect("contacts.sqlite")


db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT,phone INTEGER,email TEXT)")
db.execute("INSERT INTO contacts(name,phone,email) VALUES('Tim',658975,'tim@gmail.com')")
db.execute("INSERT INTO contacts(name,phone,email) VALUES('Rim',65588975,'Rim@gmail.com')")
db.execute("INSERT INTO contacts(name,phone,email) VALUES('Kim',658975,'Kim@gmail.com')")


cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")


#print(cursor.fetchall())
#cursor is a generators

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name,phone,email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)


cursor.close()
db.commit()
db.close()
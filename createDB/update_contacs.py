import sqlite3


db = sqlite3.connect("contacts.sqlite")
update_sql = "UPDATE contacts SET email ='update@update.com' WHERE contacts.name = 'Tim'"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("Number of rows updated:", update_cursor.rowcount)

print()
print("Are connections the same {}".format(update_cursor.connection == db))

update_cursor.connection.commit()

update_cursor.close()

for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()



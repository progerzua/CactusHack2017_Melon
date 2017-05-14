import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
#t = (str(acc.id),)
#c.execute('SELECT names FROM Teams WHERE acc_id=?', t)
c.execute("SELECT * from Users")
result = c.fetchone()
print(result)

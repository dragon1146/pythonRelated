import sqlite3


conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees01(
fname text,
lname text,
pay integer   
)""")
c.execute("INSERT INTO employees01 VALUES ('sally', 'doe', 5000)")
c.execute("INSERT INTO employees01 VALUES ('tammy', 'lee', 10000)")
c.execute("INSERT INTO employees01 VALUES ('john', 'smith', 10)")

c.execute("SELECT * FROM employees01 WHERE fname='tammy'")

print(c.fetchall())

conn.commit()

conn.close()
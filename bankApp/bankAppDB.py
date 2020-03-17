import sqlite3
from bankApp import Member



conn = sqlite3.connect('bankApp.db')

c = conn.cursor()

# c.execute("""CREATE TABLE members(
# fname text,
# lname text, 
# bal integer   
# )""")
# THIS BOC WILL CREATE 2 MEMBER OBJS WITH THE FOLLOWING ATTRIBUTES
# THIS PROCESS IS CURRENTLY DONE WITH STATIC ENTRIES BUT WILL BE CHANGED TO 
# DYNAMIC ENTRIES PROVIDED BY THE USER 

print("Enter member's first name")
print()
fname = input(">")	

print("Enter member's last name")
print()
lname = input(">")

print("Enter member's initial deposit")
print() 
initdeposit = int(input(">"))	
mem01 = Member(fname,lname, initdeposit)
# mem02 = Member('bob','smith', 2)


# THIS BOC WILL INSERT THE NEW MEMBERS WITH THEIR ATTRIBUTES IN TO THE TABLE CALLED MEMBERS
c.execute("INSERT INTO Members VALUES (:first, :last, :bal)", {'first':mem01.fname, 'last':mem01.lname, 'bal':mem01.bal})
# c.execute("INSERT INTO Members VALUES (:first, :last, :bal)", {'first':mem02.fname, 'last':mem02.lname, 'bal':mem02.bal})


# THIS BOC WILL LOOK FOR THE MEMBER WITH THE FIRST NAME OF MEM01.FNAME THEN RETURN THEIR RECORD
c.execute("SELECT * FROM members WHERE fname = :fname", {'fname': mem01.fname})
print(c.fetchall())


# THIS BOC IS SUPPOSE TO DEPOSIT $50 INTO mem01 ACCT
mem01.deposit(50)
c.execute("""UPDATE members SET bal = :bal
WHERE fname = :fname AND lname = :lname""",
{'fname': mem01.fname, 'lname': mem01.lname, 'bal': mem01.bal})
c.execute("SELECT * FROM members WHERE fname = :fname", {'fname': mem01.fname})
print(c.fetchall())


# THIS BOC IS SUPPOSE TO WITHDRAW $20 FROM MEM01 ACCT
mem01.withdraw(20)
c.execute("""UPDATE members SET bal = :bal
WHERE fname = :fname AND lname = :lname""",
{'fname': mem01.fname, 'lname': mem01.lname, 'bal': mem01.bal})
c.execute("SELECT * FROM members WHERE fname = :fname", {'fname': mem01.fname})
print(c.fetchall())

conn.commit()

conn.close()
import sqlite3



def withdraw():
    print("Enter member's first name")
    print()
    fname = input(">")	

    print("Enter member's last name")
    print()
    lname = input(">")

    print("Enter the amount of money to be withdrawn")
    print() 
    withdrawamt = int(input(">"))
    
    
    
    # USE MEM's FNAME AND LNAME TO RETRIEVE THEIR RECORD
    # GET THE MEM's BAL AND SAVE IT TO A VAR
    # IF THE BAL OF MEM's ACCT IS LESS THAN THE WITHDRAWAMT DISPLAY MESSAGE TO USER
    # IF THE BAL OF MEM's ACCT IS MORE THAN THE WITHDRAWAMT MINUS THE WITHDRAWAMT FROM BAL AND SAVE TO VAR
    # UPDATE THE RECORD OF THE MEM BY SAVING THE NEW CALCULATED BAL TO THE BAL ROW
    # COMMIT THE CHANGES TO THE DATABASE AND DISPLAY THE MEM's NEW RECORD

    if amtwithdraw > self.bal:
        print("Not enough money in account for transaction")
    # print("{}" "*5 {}" "*5 {}".format("First Name", "Last Name","Account Balance"))
    else:
        self.bal = self.bal - amtwithdraw
    # print("{}" "*5 {}" "*5 {}".format("First Name", "Last Name","Account Balance"))
    # print("{}" "*5 {}" "*5 {}{}\n".format(member01.fname, member01.lname,"$", member01.bal))
    
    # # THIS BOC IS SUPPOSE TO DEPOSIT $50 INTO mem01 ACCT
    # mem01.deposit(50)
    # c.execute("""UPDATE members SET bal = :bal
    # WHERE fname = :fname AND lname = :lname""",
    # {'fname': mem01.fname, 'lname': mem01.lname, 'bal': mem01.bal})
    # c.execute("SELECT * FROM members WHERE fname = :fname", {'fname': mem01.fname})
    # print(c.fetchall())












class Member:
	bal = 5
	def __init__(self, fname, lname, initdeposit):
		self.fname = fname
		self.lname = lname
		self.initdeposit = initdeposit
		self.bal = initdeposit + 5
        # print("{}" "*5 {}" "*5 {}".format("First Name", "Last Name","Account Balance"))
        # print("{}" "*5 {}" "*5 {}{}\n".format(member01.fname, member01.lname,"$", member01.bal))

# THIS BOC WILL IS A FUNC THAT WILL CONX TO AN EXISTING DB AND INSERT A NEW MEMBER INTO THAT DB WITH THE
# THE ATTRIBUTES OF A NEW MEMBER OBJ.
# THE OBJ WILL BE CREATED FROM INPUT FROM THE USER
def addMemToDB():
    # THIS BOC WILL REQUEST INFO FOR A NEW MEMBER THEN CREATE A NEW MEM OBJ BASED ON THAT INFO
    # THAT INFO WILL BE INSERTED IN THE MEMBER TABLE IN THE BANKAPP DB BY A FUNC CALLED addMemToDB
    
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
    
    
    conn = sqlite3.connect("bankAppdb.db")
    c = conn.cursor()
    # THIS BOC WILL INSERT THE NEW MEMBERS WITH THEIR ATTRIBUTES IN TO THE TABLE CALLED MEMBERS
    c.execute("INSERT INTO Members VALUES (:first, :last, :bal)", {'first':mem01.fname, 'last':mem01.lname, 'bal':mem01.bal})

    # THIS BOC WILL COMMIT CHANGES MADE TO THE DB THEN CLOSE THE DB
    conn.commit()    
    conn.close()
		





    
# def withdraw (self, amtwithdraw):
#     if amtwithdraw > self.bal:
#         print("Not enough money in account for transaction")
#         # print("{}" "*5 {}" "*5 {}".format("First Name", "Last Name","Account Balance"))
#     else:
#         self.bal = self.bal - amtwithdraw
#     # print("{}" "*5 {}" "*5 {}".format("First Name", "Last Name","Account Balance"))
#     # print("{}" "*5 {}" "*5 {}{}\n".format(member01.fname, member01.lname,"$", member01.bal))


# def createDB(dbName):
    # conn = sqlite3.connect(dbName)

    # c = conn.cursor()

#     c.execute("""CREATE TABLE members(
#     fname text,
#     lname text, 
#     bal integer   
#     )""")
# THIS BOC WILL CREATE 2 MEMBER OBJS WITH THE FOLLOWING ATTRIBUTES
# THIS PROCESS IS CURRENTLY DONE WITH STATIC ENTRIES BUT WILL BE CHANGED TO 
# DYNAMIC ENTRIES PROVIDED BY THE USER 

# print("Enter the name of the database")
# print()
# dbName = input(">")
# createDB(dbName)

# print("Enter member's first name")
# print()
# fname = input(">")	

# print("Enter member's last name")
# print()
# lname = input(">")

# print("Enter member's initial deposit")
# print() 
# initdeposit = int(input(">"))	
# mem01 = Member(fname,lname, initdeposit)
# mem02 = Member('bob','smith', 2)

# conn = sqlite3.connect(dbName)

# c = conn.cursor()
# # THIS BOC WILL INSERT THE NEW MEMBERS WITH THEIR ATTRIBUTES IN TO THE TABLE CALLED MEMBERS
# c.execute("INSERT INTO Members VALUES (:first, :last, :bal)", {'first':mem01.fname, 'last':mem01.lname, 'bal':mem01.bal})
# c.execute("INSERT INTO Members VALUES (:first, :last, :bal)", {'first':mem02.fname, 'last':mem02.lname, 'bal':mem02.bal})


# THIS BOC WILL LOOK FOR THE MEMBER WITH THE FIRST NAME OF MEM01.FNAME THEN RETURN THEIR RECORD
# c.execute("SELECT * FROM members WHERE fname = :fname", {'fname': mem01.fname})
# print(c.fetchall())


# # THIS BOC IS SUPPOSE TO DEPOSIT $50 INTO mem01 ACCT
# mem01.deposit(50)
# c.execute("""UPDATE members SET bal = :bal
# WHERE fname = :fname AND lname = :lname""",
# {'fname': mem01.fname, 'lname': mem01.lname, 'bal': mem01.bal})
# c.execute("SELECT * FROM members WHERE fname = :fname", {'fname': mem01.fname})
# print(c.fetchall())


# # THIS BOC IS SUPPOSE TO WITHDRAW $20 FROM MEM01 ACCT
# mem01.withdraw(20)
# c.execute("""UPDATE members SET bal = :bal
# WHERE fname = :fname AND lname = :lname""",
# {'fname': mem01.fname, 'lname': mem01.lname, 'bal': mem01.bal})
# c.execute("SELECT * FROM members WHERE fname = :fname", {'fname': mem01.fname})
# print(c.fetchall())

# conn.commit()

# conn.close()
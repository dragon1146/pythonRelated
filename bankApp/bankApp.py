class Member:
	bal = 5
	def __init__(self, fname, lname, initdeposit):
		self.fname = fname
		self.lname = lname
		self.initdeposit = initdeposit
		self.bal = initdeposit + 5
        # print("{}" "*5 {}" "*5 {}".format("First Name", "Last Name","Account Balance"))
        # print("{}" "*5 {}" "*5 {}{}\n".format(member01.fname, member01.lname,"$", member01.bal))
		
	def deposit(self, amtdeposit):
		self.bal = self.bal + amtdeposit
        # print("{}" "*5 {}" "*5 {}".format("First Name", "Last Name","Account Balance"))
        # print("{}" "*5 {}" "*5 {}{}\n".format(member01.fname, member01.lname,"$", member01.bal))
		
	def withdraw (self, amtwithdraw):
		if amtwithdraw > self.bal:
		    print("Not enough money in account for transaction")
            # print("{}" "*5 {}" "*5 {}".format("First Name", "Last Name","Account Balance"))
		else:
			self.bal = self.bal - amtwithdraw
        # print("{}" "*5 {}" "*5 {}".format("First Name", "Last Name","Account Balance"))
        # print("{}" "*5 {}" "*5 {}{}\n".format(member01.fname, member01.lname,"$", member01.bal))


# print("Enter member's first name")
# print()
# fname = input(">")	

# print("Enter member's last name")
# print()
# lname = input(">")

# print("Enter member's initial deposit")
# print() 
# initdeposit = int(input(">"))	
			
				
	
# member01 = Member(fname, lname, initdeposit)

# print("{}\n{}\n{}{}\n".format(member01.fname, member01.lname,"$", member01.bal))


# member01.deposit(50)
# print("{}\n{}\n{}{}\n".format(member01.fname, member01.lname,"$", member01.bal))

	
# member01.withdraw(10)		
# print("{}\n{}\n{}{}\n".format(member01.fname, member01.lname,"$", member01.bal))
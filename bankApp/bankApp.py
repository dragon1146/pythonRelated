

# CREATE CLASS FOR MEMBERS WITH THE FOLLOWING
#   - CONSTRUCTOR THAT STARTS EVERY ACCT WITH $5.00
#   - METHOD FOR DEPOSITES
#   - METHOD FOR WITHDRAWS
#   - CLASS ATTRIBUTES
#       - MEMBER FIRST NAME
#       - MEMBER LAST NAME

#   - REQUEST INPUT FROM USER WITH THE FOLLOWING INFO FOR MEMBER
#       - FIRST NAME
#       - LAST NAME
#       - INITIAL DEPOSIT

#   - CREATE AN OBJ FOR THAT NEW MEMBER WITH THE INFO RECIEVED FROM THE USER
#   - DISPLAY THE INFO AFTER THE OBJECT HAS BEEN CREATED
#############################################################################
#############################################################################

#   - CONSTRUCTOR THAT STARTS EVERY ACCT WITH THE FOLLOWING:
#       - INITIAL ACCT BALANCE OF $5.00 OR MORE
#       - THE FOLLOWING CLASS ATTRIBUTES
#           - MEMBER FIRST NAME
#           - MEMBER LAST NAME
#       - METHOD FOR DEPOSITES
#       - METHOD FOR WITHDRAWS

class Member:
#   - CONSTRUCTOR THAT STARTS EVERY ACCT WITH THE FOLLOWING:
#       - INITIAL ACCT BALANCE OF $5.00 OR MORE
#       - THE FOLLOWING CLASS ATTRIBUTES
#           - MEMBER FIRST NAME
#           - MEMBER LAST NAME
#def __int__(self, startBalance, fName, lName):
    def __int__(self):
        if startBalance <= 5:
            self.balance = startBalance + 5
        else:
            self.balance = startBalance
        
        # self.fName = fName
        # self.lName = lName


#   - METHOD FOR DEPOSITES
    def deposit(self, amtDepoit):
        self.balance = self.balance + amtDepoit
        print(self.balance)


#   - METHOD FOR WITHDRAWS
    def withdraw(self, amtWithdraw):
        if amtWithdraw > self.balance:
            print("Not enought in account for this transaction")
            print(self.balance)
        else:
            self.balance = self.balance - amtWithdraw
            print(self.balance)



#   - CREATE AN OBJ FOR THAT NEW MEMBER WITH THE INFO RECIEVED FROM THE USER
print("Enter member's first name")
print
fName = input(">")
print("Enter member's last name")
print
lName = input(">")
print("Enter member's first deposit")
print
startBalance = int(input(">"))
print
print("*******************************************************")
# THIS BOC WILL CREATE THE MEMBER OBJ AND SAVE IT TO A VARIABLE CALLED MEMBER01
# TO ACCOUNT FOR HAVING TO CREATE MULTIPLE MEMBERS THE LAST TWO DIGITS CAN BE 
# CREATED WITH THE RANDOM FUNC OR SOME KIND OF COUNTER
member01 = Member()
fName = fName
startBalance = startBalance
lName = lName
# THIS BOC WILL DISPLAY THE PROPERTIES OF MEMBER01 ONCE THE OBJ HAS BEEN CREATED
print("The following member account was created")
print(member01.fName + member01.lName)
print(member01.balance)
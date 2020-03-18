





def createNewDatabase():
    print("Enter the name of the database")
    print()
    dbName = input(">")

    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    conn.commit()    
    conn.close()
    c.execute("""CREATE TABLE members(
    fname text,
    lname text, 
    bal integer   
    )""")





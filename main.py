#Exercise 13
import sqlite3 as sql
"""con = sql.connect('library.db')
res = con.execute("SELECT * FROM Loans")
print(res.fetchall())
con.close()

#Exercise 14
#1. Generates all Loans even though the user doesn't know the mid
#2. If they input "Loans.mid", it functions the same as TRUE
#3. Have constraints where they can only input numbers, catch these "all" cases,
    #or only accept values in the columns
con = sql.connect('library.db')
u_input = input("Try to hack me >:)")
res = con.execute(f"SELECT * FROM Loans L WHERE L.mid = ?{u_input}")
print(res.fetchall())
u_input = input("Try to hack me (again) >:)")
res = con.execute(f"SELECT * FROM Loans L WHERE L.mid = :{u_input}")
print(res.fetchall())
con.close()

#Exercise 15
#IV. UPDATE, DELETE, and SELECT (?)
#V. All execute SQL statements, execute is good for single, implicit transactions,
    #executemany is good for entires that are essentially the same, other than the a single variable
    #, and executescript is good for multiple entries, normally explicit transactions
con = sql.connect('library.db')
con.execute("CREATE TABLE IF NOT EXISTS Games(gid INTEGER PRIMARY KEY, title TEXT NOT NULL, platform TEXT NOT NULL);")
games = [tuple((1, "Baldur's Gate 3", "PC")), tuple((2, "Animal Crossing", "Switch")), tuple((3, "House Flipper", "PC"))]
insert = con.executemany("INSERT INTO Games VALUES(?,?,?)", games)
con.commit()
print(insert.rowcount)
print(con.total_changes)
con.close()

#Exercise 16
#IV. fetchone and fetchmany both fetch a set number of tuples, 1 for one and size for fetchmany
    #fetchone is consistent but fetchmany is flexible
con = sql.connect('library.db')
res = con.execute("SELECT * FROM Loans")
for index in res:
    print(res.fetchmany(2))
con.close()"""
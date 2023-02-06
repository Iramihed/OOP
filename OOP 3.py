import sqlite3 as sl
con=sl.connect('')
curs=con.cursor()
c="""CREATE TABLE IF NOT EXISTS expensis (id INTEGER, name TEXT)"""
c="""INC"""
curs.execute(c)




curs.close()
con.close()







import pyodbc
import myFunction

conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=localhost\SQLEXPRESS;" "Database=scuola;" "Trusted_Connection=yes;")
'''cursor=conn.cursor()
try:
    cursor.execute("INSERT INTO Studente (Nome, Cognome, Indirizzo, Cap, Tel, Nascita) "
               "VALUES ('Maria' , 'Bianchi', 'Via L. Ariosto 9, Ferrara (FE)', '44121', '3483483483', '19921123')")
    conn.commit()
except:
    conn.rollback()
cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='Studente'")
for row in cursor:
    print('row = %r' % (row[3],))
'''
myFunction.printTable(conn, "Studente")
conn.close()
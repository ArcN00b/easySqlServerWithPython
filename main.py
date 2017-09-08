import pyodbc
import myFunction

# Connessione al Database
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=localhost\SQLEXPRESS;" "Database=scuola;" "Trusted_Connection=yes;")

myFunction.printTable(conn, "Studente")

# Chiusura della connessione
conn.close()
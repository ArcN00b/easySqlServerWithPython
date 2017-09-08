#Funzione che stampa una tabella completa di struttura
def printTable(conn, name):

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='" + name +"'")
    #for row in cursor:
    print('row = %r' % (cursor))
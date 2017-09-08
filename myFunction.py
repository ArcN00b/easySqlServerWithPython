#Funzione che stampa una tabella completa di struttura
def printTable(conn, name):

    # Connessione al database per ottenere l'informazione sulla tabella
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='" + name + "'")

    # Stampa della cornice superiore

    # Stampa della struttura
    print("|", end="")
    for row in cursor:
        #print("         %s          |" % (row[3]), end="")
        print("%s" % (row))
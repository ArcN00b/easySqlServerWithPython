#Funzione che stampa una tabella completa di struttura
def printTable(conn, name):

    # Connessione al database per ottenere l'informazione sulla tabella
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='" + name + "'")

    # Stampa della cornice superiore
    print("+", end="")
    for row in cursor:
        for num in range(0,len(row[3])+7):
            print("-", end="")
        print("+", end="")

    # Stampa della struttura
    print("|", end="")
    for row in cursor:
        print("    %s  |" % (row[3]), end="")

    # Stampa della cornice inferiore
    print("+", end="")
    for row in cursor:
        for num in range(0,len(row[3])+7):
            print("-", end="")
        print("+", end="")
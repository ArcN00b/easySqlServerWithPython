#Funzione che stampa una tabella completa di struttura
def printTable(conn, name):

    # Connessione al database per ottenere l'informazione sulla tabella
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + name)
    results = cursor.fetchall()

    widths = []
    columns = []
    tavnit = '|'
    separator = '+'

    for cd in cursor.description:
        widths.append(max(cd[2], len(cd[0])))
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-" + "%ss |" % (w,)
        separator += '-' * w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator)


#"VALUES ('Maria' , 'Bianchi', 'Via L. Ariosto 9, Ferrara (FE)', '44121', '3483483483', '19921123')")
def insertIntoStudenti(conn, values):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Studente (Nome, Cognome, Indirizzo, Cap, Tel, Nascita) "
                   "VALUES (" + values +")")
        conn.commit()
        print("Operazione completata")
    except:
        conn.rollback()

#Funzione che stampa una tabella completa di struttura
def printTable(conn, name):

    # Connessione al database per ottenere l'informazione sulla tabella
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + name)
    results = cursor.fetchall()

    # Variabili locali utili per formattare correttamente la stampa
    widths = []
    columns = []
    tavnit = '|'
    separator = '+'

    # Controllo della larghezza delle varie colonne
    for cd in cursor.description:
        widths.append(max(len(cd[0]), cd[4]))
        columns.append(cd[0])

    # Aggiunta della quantità di simboli da inserire per la corretta formattazione
    for w in widths:
        tavnit += " %-" + "%ss |" % (w,)
        separator += '-' * w + '--+'

    # Stampa dei dati formattati
    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % tuple(row))
    print(separator)
    print("")


#"VALUES ('Maria' , 'Bianchi', 'Via L. Ariosto 9, Ferrara (FE)', '44121', '3483483483', '19921123')")
def insertInto(conn, name, attributes, values):
    cursor = conn.cursor()
    try:
        "Nome, Cognome, Indirizzo, Cap, Tel, Data di nascita, Dipartimento"
        cursor.execute("INSERT INTO "+ name +" (" + attributes +") "
                   "VALUES (" + values +")")
        conn.commit()
        print("Operazione completata")
    except:
        conn.rollback()
        print("Errore durante l'operazione")

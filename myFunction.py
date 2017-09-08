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
    print(name)
    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % tuple(row))
    print(separator)
    print("")


def insertInto(conn, name, attributes, values):
    cursor = conn.cursor()
    try:
        #"Trovo il numero esatto di ? da inserire nel campo values
        questions = "?, " * len(values)
        questions = questions[:-2]
        cursor.execute("INSERT INTO " + name + " (" + attributes + ") VALUES (" + questions + ")", values)
        conn.commit()
        print("Operazione completata")
    except Exception as e:

        conn.rollback()
        print(e)

def deleteFrom(conn, name, attribute, value):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + name + " WHERE " + attribute + " = '" + value +"'")
    print(len(cursor))
    try:
        cursor.execute("DELETE FROM " + name + " WHERE " + attribute + " = '" + value +"'")
        conn.commit()
        print("Operazione completata")
    except Exception as e:

        conn.rollback()
        print(e)
#Funzione che controlla se esiste il valore dell'attributo nella tabella name
def check(conn, name, attribute, value):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + name + " WHERE " + attribute + " = '" + value + "'")
    if cursor.rowcount == 0:
        return False
    else:
        return True

#Funzione che controlla il numero di esami presenti per uno studente di un gruppo
def checkExams(conn, values):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Studente WHERE Matricola_Stud = '" + values[-2] + "' AND ID_Gruppo = '" + values[-1] + "'")
    if cursor.rowcount < 3:
        return True
    else:
        return False

#Funzione che stampa una tabella completa di struttura
def printTable(conn, query):

    # Connessione al database per ottenere l'informazione sulla tabella
    cursor = conn.cursor()
    cursor.execute(query)
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
    if(len(query.split(" ")[-1]) < 25):
        print(query.split(" ")[-1])
    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % tuple(row))
    print(separator)
    print("")

# Funzione che inserisce i valori all'interno delle tuple utilizzando gli attributi
def insertInto(conn, name, attributes, values):
    cursor = conn.cursor()
    try:
        # Trovo il numero esatto di ? da inserire nel campo values
        questions = "?, " * len(values)
        questions = questions[:-2]
        cursor.execute("INSERT INTO " + name + " (" + attributes + ") VALUES (" + questions + ")", values)
        conn.commit()
        print("Operazione completata")
    except Exception as e:
        conn.rollback()
        print(e)

# Funzione che cancella le tuple utilizzando gli attributi
def deleteFrom(conn, name, attribute, value):
    if check(conn, name, attribute, value) == False:
        print(attribute + " inserito non esiste all'interno del database")
    else:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM " + name + " WHERE " + attribute + " = '" + value +"'")
            conn.commit()
            print("Operazione completata")
        except Exception as e:
            conn.rollback()
            print(e)

def update(conn, name, attributes, values, condition):
    cursor = conn.cursor()
    try:
        # Creo la stringa da usare come query
        query = "UPDATE " + name + " SET "
        for num in range(0, len(attributes)):
            query = query + attributes[num] + " = '" + values[num] + "', "
        query = query[:-2] + " WHERE " + condition
        cursor.execute(query)
        conn.commit()
        print("Operazione completata")
    except Exception as e:
        conn.rollback()
        print(e)
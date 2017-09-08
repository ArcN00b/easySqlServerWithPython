import pyodbc
import os
import myFunction

# Connessione al Database
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=localhost\SQLEXPRESS;" "Database=scuola;" "Trusted_Connection=yes;")

# Stampa del menù
print(30 * '-')
print("             MENU PRINCIPALE  ")
print(30 * '-')
print("1. Inserimento")
print("2. Visualizzazione")
print("3. Reboot the server")
print(30 * '-')

# Input della scelta
choose = input()

# Menù inserimento
if choose == "1":
    print("             MENU INSERIMENTO  ")
    print(30 * '-')
    print("1. Inserisci docente")
    print("2. Inserisci studente")
    print("3. Inserisci risultato esame")
    print("4. Inserisci tipo esercitazione")
    print("5. Inserisci programma d'esame")
    print("6. Inserisci gruppo di esercitazioni")
    print("7. Inserisci frequenza ai corsi")
    print("8. Torna al menu precedente")

    # Input della scelta
    choose = input()

    # Inserimento nuovo docente
    if choose == "1":

        # Stampo i docenti già presenti
        myFunction.printTable(conn, "Docente")

        # Richiedo i dati e li preparo per la query
        campi = ["Nome", "Cognome", "Indirizzo", "Cap", "Tel", "Data di nascita", "Dipartimento"]
        valori = []
        for n in campi:
            print(n + " = ", end="")
            temp = input()
            valori.append(temp)

        # Eseguo la query di inserimento
        attributi = "Nome, Cognome, Indirizzo, Cap, Tel, Nascita, Dipartimento"
        myFunction.insertInto(conn, "Docente", attributi, valori)

    # Inserimento nuovo studente
    if choose == "2":

        # Stampo gli studenti già presenti
        myFunction.printTable(conn, "Studente")

        # Richiedo i dati e li preparo per la query
        campi = ["Nome", "Cognome", "Indirizzo", "Cap", "Tel", "Data di nascita"]
        valori = []
        for n in campi:
            print(n + " = ", end="")
            temp = input()
            valori.append(temp)

        # Eseguo la query di inserimento
        attributi = "Nome, Cognome, Indirizzo, Cap, Tel, Nascita"
        myFunction.insertInto(conn, "Studente", attributi, valori)

    #Inserimento nuovo esame
    #TODO aggiunta di collegamento tra esame e materia
    if choose == "3":

        # Stampo gli studenti già presenti
        myFunction.printTable(conn, "Studente")

        # Richiedo i dati e li preparo per la query
        campi = ["Voto", "Lode", "Data", "Matricola"]
        valori = []
        for n in campi:
            print(n + " = ", end="")
            temp = input()
            valori.append(temp)

        # Eseguo la query di inserimento
        attributi = "Voto, Lode, Data, Matricola_Stud"
        myFunction.insertInto(conn, "Esame", attributi, valori)

    # Inserimento nuovo tipo di esercitazione
    if choose == "4":

        # Stampo i tipi già presenti
        myFunction.printTable(conn, "Tipo")

        # Richiedo i dati e li preparo per la query
        campi = ["Tipo", "Frontale"]
        valori = []
        for n in campi:
            print(n + " = ", end="")
            temp = input()
            valori.append(temp)

        # Eseguo la query di inserimento
        attributi = "Tipo, Frontale"
        myFunction.insertInto(conn, "Tipo", attributi, valori)

    # Inserimento nuovo programma d'esame
    if choose == "5":

        # Stampo i programmi
        myFunction.printTable(conn, "Programma")

        # Richiedo i dati e li preparo per la query
        campi = ["Descrizione", "Bibliografia"]
        valori = []
        for n in campi:
            print(n + " = ", end="")
            temp = input()
            valori.append(temp)

        # Eseguo la query di inserimento
        attributi = "Descrizione, Bibliografia"
        myFunction.insertInto(conn, "Programma", attributi, valori)

    # Inserimento nuovo gruppo di esercitazioni
    if choose == "6":

        # Stampo i gruppi, i docenti, i tipi di esercitazione e i programmi d'esame
        myFunction.printTable(conn, "Gruppo")
        myFunction.printTable(conn, "Docente")
        myFunction.printTable(conn, "Tipo")
        myFunction.printTable(conn, "Programma")

        # Richiedo i dati e li preparo per la query
        campi = ["Orario", "Anno Accademico", "Tipo Esercitazione", "Matricola Docente", "Programma"]
        valori = []
        for n in campi:
            print(n + " = ", end="")
            temp = input()
            valori.append(temp)

        # Eseguo la query di inserimento
        attributi = "Orario, Anno_Accademico, ID_Tipo, Matricola_Doc, ID_Pro"
        myFunction.insertInto(conn, "Gruppo", attributi, valori)

    # Inserimento nuova partecipazione
    if choose == "7":

        # Stampo le partecipazioni, gli studenti e i gruppi
        myFunction.printTable(conn, "Partecipa")
        myFunction.printTable(conn, "Studente")
        myFunction.printTable(conn, "Gruppo")

        # Richiedo i dati e li preparo per la query
        campi = ["Matricola", "Gruppo"]
        valori = []
        for n in campi:
            print(n + " = ", end="")
            temp = input()
            valori.append(temp)

        # Eseguo la query di inserimento
        attributi = "Matricola_Stud, ID_Gruppo"
        myFunction.insertInto(conn, "Partecipa", attributi, valori)

    if choose == "8":
        os.system("cls")

# Chiusura della connessione
conn.close()
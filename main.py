import pyodbc
import os
import myFunction

# Connessione al Database
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=localhost\SQLEXPRESS;" 
                      "Database=scuola;" "Trusted_Connection=yes;")

# Stampa del menù
print(30 * '-')
print("             MENU PRINCIPALE  ")
print(30 * '-')
print("1. Inserimento")
print("2. Visualizzazione")
print("3. Cancellazione")
print("4. Modifica")
print(30 * '-')

# Input della scelta
choose = input()

# Menù inserimento
if choose == "1":

    # Ripeto finchè la scelta non è 8
    while choose != "8":
        print("   MENU INSERIMENTO  ")
        print(30 * '-')
        print("1. Inserisci docente")
        print("2. Inserisci studente")
        print("3. Inserisci risultato esame")
        print("4. Inserisci tipo esercitazione")
        print("5. Inserisci programma d'esame")
        print("6. Inserisci gruppo di esercitazioni")
        print("7. Inserisci partecipazione ad un gruppo")
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
                while len(temp) == 0:
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
                while len(temp) == 0:
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
                while len(temp) == 0:
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
                while len(temp) == 0:
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
                while len(temp) == 0:
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
                while len(temp) == 0:
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
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la query di inserimento
            attributi = "Matricola_Stud, ID_Gruppo"
            myFunction.insertInto(conn, "Partecipa", attributi, valori)

        if choose == "8":
            os.system("cls")

# Menù inserimento
if choose == "2":

    # Ripeto finchè la scelta non è 9
    while choose != "9":
        print("   MENU VISUALIZZAZIONE  ")
        print(30 * '-')
        print("1. Visualizza docenti")
        print("2. Visualizza studenti")
        print("3. Visualizza gli esami svolti")
        print("4. Visualizza i tipi di esercitazione")
        print("5. Visualizza i programmi d'esame")
        print("6. Visualizza i gruppi di esercitazioni")
        print("7. Visualizza la partecipazione ai gruppi")
        print("8. Visualizza intero database")
        print("9. Torna al menu precedente")

        # Input della scelta
        choose = input()

        # Visualizzazione scelta
        if choose == "1":
            myFunction.printTable(conn, "Docente")
        if choose == "2":
            myFunction.printTable(conn, "Studente")
        if choose == "3":
            myFunction.printTable(conn, "Esame")
        if choose == "4":
            myFunction.printTable(conn, "Tipo")
        if choose == "5":
            myFunction.printTable(conn, "Programma")
        if choose == "6":
            myFunction.printTable(conn, "Gruppo")
        if choose == "7":
            myFunction.printTable(conn, "Partecipa")
        if choose == "8":
            myFunction.printTable(conn, "Docente")
            myFunction.printTable(conn, "Studente")
            myFunction.printTable(conn, "Esame")
            myFunction.printTable(conn, "Tipo")
            myFunction.printTable(conn, "Programma")
            myFunction.printTable(conn, "Gruppo")
            myFunction.printTable(conn, "Partecipa")
        if choose == "9":
            os.system("cls")

if choose == "3":

    # Ripeto finchè la scelta non è 9
    while choose != "8":
        print("   MENU CANCELLAZIONE  ")
        print(30 * '-')
        print("1. Cancella docente")
        print("2. Cancella studente")
        print("3. Cancella un esame svolto")
        print("4. Cancella un tipo di esercitazione")
        print("5. Cancella un programma d'esame")
        print("6. Cancella un gruppo di esercitazioni")
        print("7. Cancella una partecipazione ai gruppi")
        print("8. Torna al menu precedente")

        # Input della scelta
        choose = input()

        # Cancellazione scelta
        if choose == "1":
            myFunction.printTable(conn, "Docente")
            print("Selezionare la matricola da rimuovere ", end="")
            matricola = input()
            myFunction.deleteFrom(conn,"Docente","Matricola", matricola)
        if choose == "2":
            myFunction.printTable(conn, "Studente")
            print("Selezionare la matricola da rimuovere ", end="")
            matricola = input()
            myFunction.deleteFrom(conn,"Studente","Matricola", matricola)
        if choose == "3":
            myFunction.printTable(conn, "Esame")
            print("Selezionare l'id da rimuovere ", end="")
            id = input()
            myFunction.deleteFrom(conn,"Esame","ID", id)
        if choose == "4":
            myFunction.printTable(conn, "Tipo")
            print("Selezionare l'id da rimuovere ", end="")
            id = input()
            myFunction.deleteFrom(conn,"Tipo","ID", id)
        if choose == "5":
            myFunction.printTable(conn, "Programma")
            print("Selezionare l'id da rimuovere ", end="")
            id = input()
            myFunction.deleteFrom(conn,"Programma","ID", id)
        if choose == "6":
            myFunction.printTable(conn, "Gruppo")
            print("Selezionare l'id da rimuovere ", end="")
            id = input()
            myFunction.deleteFrom(conn,"Gruppo","ID", id)
        if choose == "7":
            myFunction.printTable(conn, "Partecipa")
            print("Selezionare l'id da rimuovere ", end="")
            id = input()
            myFunction.deleteFrom(conn,"Partecipa","ID", id)
        if choose == "8":
            os.system("cls")

if choose == "4":
    print("   MENU MODIFICA ")
    print(30 * '-')
    print("1. Modifica docente")
    print("2. Modifica studente")
    print("3. Modifica un esame svolto")
    print("4. Modifica un tipo di esercitazione")
    print("5. Modifica un programma d'esame")
    print("6. Modifica un gruppo di esercitazioni")
    print("7. Modifica una partecipazione ai gruppi")
    print("8. Torna al menu precedente")

    # Input della scelta
    choose = input()

    # Cancellazione scelta
    if choose == "1":

        # Chiedo la matricola in input
        myFunction.printTable(conn, "Docente")
        print("Selezionare la matricola da modificare ", end="")
        matricola = input()

        # Controllo che la matricola inserita esista
        if myFunction.check(conn, "Docente", "Matricola", matricola):

            # Richiedo tutti gli altri campi
            campi = ["Nome", "Cognome", "Indirizzo", "Cap", "Tel", "Data di nascita", "Dipartimento"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            myFunction.update(conn, "Docente", campi, valori, "Matricola = '" + matricola + "'")

        # Se la matricola non esiste scrivo messaggio d'errore
        else:
            print("La matricola scelta non esiste")
    if choose == "2":
        myFunction.printTable(conn, "Studente")
        print("Selezionare la matricola da rimuovere ", end="")
        matricola = input()
        myFunction.deleteFrom(conn,"Studente","Matricola", matricola)
    if choose == "3":
        myFunction.printTable(conn, "Esame")
        print("Selezionare l'id da rimuovere ", end="")
        id = input()
        myFunction.deleteFrom(conn,"Esame","ID", id)
    if choose == "4":
        myFunction.printTable(conn, "Tipo")
        print("Selezionare l'id da rimuovere ", end="")
        id = input()
        myFunction.deleteFrom(conn,"Tipo","ID", id)
    if choose == "5":
        myFunction.printTable(conn, "Programma")
        print("Selezionare l'id da rimuovere ", end="")
        id = input()
        myFunction.deleteFrom(conn,"Programma","ID", id)
    if choose == "6":
        myFunction.printTable(conn, "Gruppo")
        print("Selezionare l'id da rimuovere ", end="")
        id = input()
        myFunction.deleteFrom(conn,"Gruppo","ID", id)
    if choose == "7":
        myFunction.printTable(conn, "Partecipa")
        print("Selezionare l'id da rimuovere ", end="")
        id = input()
        myFunction.deleteFrom(conn,"Partecipa","ID", id)
    if choose == "8":
        os.system("cls")

# Chiusura della connessione
conn.close()
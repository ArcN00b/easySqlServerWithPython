import pyodbc
import os
import myFunction

# Connessione al Database
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=localhost\SQLEXPRESS;" 
                      "Database=scuola;" "Trusted_Connection=yes;")

# Stampa del menù
#TODO aggiungere ciclo while al termine delle modifiche
print(30 * '-')
print("             MENU PRINCIPALE  ")
print(30 * '-')
print("1. Inserimento")
print("2. Visualizzazione")
print("3. Cancellazione")
print("4. Modifica")
print("5. Ricerca")
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
            myFunction.printTable(conn, "SELECT * FROM Docente")

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
            myFunction.printTable(conn, "SELECT * FROM Studente")

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
        if choose == "3":

            # Stampo gli studenti già presenti
            myFunction.printTable(conn, "SELECT * FROM Studente")
            myFunction.printTable(conn, "SELECT * FROM Partecipa")
            myFunction.printTable(conn, "SELECT * FROM Gruppo")
            myFunction.printTable(conn, "SELECT * FROM Esame")

            # Richiedo i dati e li preparo per la query
            campi = ["Voto", "Lode", "Tipo", "Data", "Matricola", "Gruppo"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la query di inserimento
            attributi = "Voto, Lode, Tipo, Data, Matricola_Stud, ID_Gruppo"
            myFunction.insertInto(conn, "Esame", attributi, valori)

        # Inserimento nuovo tipo di esercitazione
        if choose == "4":

            # Stampo i tipi già presenti
            myFunction.printTable(conn, "SELECT * FROM Tipo")

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
            myFunction.printTable(conn, "SELECT * FROM Programma")

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
            myFunction.printTable(conn, "SELECT * FROM Gruppo")
            myFunction.printTable(conn, "SELECT * FROM Docente")
            myFunction.printTable(conn, "SELECT * FROM Tipo")
            myFunction.printTable(conn, "SELECT * FROM Programma")

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
            myFunction.printTable(conn, "SELECT * FROM Partecipa")
            myFunction.printTable(conn, "SELECT * FROM Studente")
            myFunction.printTable(conn, "SELECT * FROM Gruppo")

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

# Menù Visualizzazione
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
            myFunction.printTable(conn, "SELECT * FROM Docente")
        if choose == "2":
            myFunction.printTable(conn, "SELECT * FROM Studente")
        if choose == "3":
            myFunction.printTable(conn, "SELECT * FROM Esame")
        if choose == "4":
            myFunction.printTable(conn, "SELECT * FROM Tipo")
        if choose == "5":
            myFunction.printTable(conn, "SELECT * FROM Programma")
        if choose == "6":
            myFunction.printTable(conn, "SELECT * FROM Gruppo")
        if choose == "7":
            myFunction.printTable(conn, "SELECT * FROM Partecipa")
        if choose == "8":
            myFunction.printTable(conn, "SELECT * FROM Docente")
            myFunction.printTable(conn, "SELECT * FROM Studente")
            myFunction.printTable(conn, "SELECT * FROM Esame")
            myFunction.printTable(conn, "SELECT * FROM Tipo")
            myFunction.printTable(conn, "SELECT * FROM Programma")
            myFunction.printTable(conn, "SELECT * FROM Gruppo")
            myFunction.printTable(conn, "SELECT * FROM Partecipa")
        if choose == "9":
            os.system("cls")

# Menù Cancellazione
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
            myFunction.printTable(conn, "SELECT * FROM Docente")
            print("Selezionare la matricola da rimuovere ", end="")
            matricola = input()
            myFunction.deleteFrom(conn,"Docente","Matricola", matricola)
        if choose == "2":
            myFunction.printTable(conn, "SELECT * FROM Studente")
            print("Selezionare la matricola da rimuovere ", end="")
            matricola = input()
            myFunction.deleteFrom(conn,"Studente","Matricola", matricola)
        if choose == "3":
            myFunction.printTable(conn, "SELECT * FROM Esame")
            print("Selezionare l'id da rimuovere ", end="")
            id = input()
            myFunction.deleteFrom(conn,"Esame","ID", id)
        if choose == "4":
            myFunction.printTable(conn, "SELECT * FROM Tipo")
            print("Selezionare l'id da rimuovere ", end="")
            id = input()
            myFunction.deleteFrom(conn,"Tipo","ID", id)
        if choose == "5":
            myFunction.printTable(conn, "SELECT * FROM Programma")
            print("Selezionare l'id da rimuovere ", end="")
            id = input()
            myFunction.deleteFrom(conn,"Programma","ID", id)
        if choose == "6":
            myFunction.printTable(conn, "SELECT * FROM Gruppo")
            print("Selezionare l'id da rimuovere ", end="")
            id = input()
            myFunction.deleteFrom(conn,"Gruppo","ID", id)
        if choose == "7":
            myFunction.printTable(conn, "SELECT * FROM Partecipa")
            print("Selezionare l'id da rimuovere ", end="")
            id = input()
            myFunction.deleteFrom(conn,"Partecipa","ID", id)
        if choose == "8":
            os.system("cls")

# Menù Modifica
if choose == "4":
    #TODO Aggiungere ciclo while al termine delle modifiche
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
        myFunction.printTable(conn, "SELECT * FROM Docente")
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
            attributi = ["Nome", "Cognome", "Indirizzo", "Cap", "Tel", "Nascita", "Dipartimento"]
            myFunction.update(conn, "Docente", attributi, valori, "Matricola = '" + matricola + "'")

        # Se la matricola non esiste scrivo messaggio d'errore
        else:
            print("La matricola scelta non esiste")
    if choose == "2":

        # Chiedo la matricola in input
        myFunction.printTable(conn, "SELECT * FROM Studente")
        print("Selezionare la matricola da modificare ", end="")
        matricola = input()

        # Controllo che la matricola inserita esista
        if myFunction.check(conn, "Studente", "Matricola", matricola):

            # Richiedo tutti gli altri campi
            campi = ["Nome", "Cognome", "Indirizzo", "Cap", "Tel", "Data di nascita"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Nome", "Cognome", "Indirizzo", "Cap", "Tel", "Nascita"]
            myFunction.update(conn, "Studente", attributi, valori, "Matricola = '" + matricola + "'")

        # Se la matricola non esiste scrivo messaggio d'errore
        else:
            print("La matricola scelta non esiste")
    if choose == "3":

        # Chiedo l'id in input
        myFunction.printTable(conn, "SELECT * FROM Esame")
        print("Selezionare l'id da modificare ", end="")
        id = input()

        # Controllo che l'id inserito esista
        if myFunction.check(conn, "Esame", "ID", id):

            # Richiedo tutti gli altri campi
            campi = ["Voto", "Lode", "Tipo", "Data", "Matricola", "Gruppo"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Voto", "Lode", "Tipo", "Data", "Matricola_Stud", "ID_Gruppo"]
            myFunction.update(conn, "Esame", attributi, valori, "ID = '" + id + "'")

        # Se l'id non esiste scrivo messaggio d'errore
        else:
            print("L'id scelto non esiste")
    if choose == "4":

        # Chiedo l'id in input
        myFunction.printTable(conn, "SELECT * FROM Tipo")
        print("Selezionare l'id da modificare ", end="")
        id = input()

        # Controllo che l'id inserito esista
        if myFunction.check(conn, "Tipo", "ID", id):

            # Richiedo tutti gli altri campi
            campi = ["Tipo", "Frontale"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Tipo", "Frontale"]
            myFunction.update(conn, "Tipo", attributi, valori, "ID = '" + id + "'")

        # Se l'id non esiste scrivo messaggio d'errore
        else:
            print("L'id scelto non esiste")
    if choose == "5":

        # Chiedo l'id in input
        myFunction.printTable(conn, "SELECT * FROM Programma")
        print("Selezionare l'id da modificare ", end="")
        id = input()

        # Controllo che l'id inserito esista
        if myFunction.check(conn, "Programma", "ID", id):

            # Richiedo tutti gli altri campi
            campi = ["Descrizione", "Bibliografia"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Descrizione", "Bibliografia"]
            myFunction.update(conn, "Programma", attributi, valori, "ID = '" + id + "'")

        # Se l'id non esiste scrivo messaggio d'errore
        else:
            print("L'id scelto non esiste")
    if choose == "6":

        # Stampo i gruppi, i docenti, i tipi di esercitazione e i programmi d'esame
        myFunction.printTable(conn, "SELECT * FROM Docente")
        myFunction.printTable(conn, "SELECT * FROM Tipo")
        myFunction.printTable(conn, "SELECT * FROM Programma")
        myFunction.printTable(conn, "SELECT * FROM Gruppo")
        print("Selezionare l'id del gruppo da modificare ", end="")
        id = input()

        # Controllo che l'id inserito esista
        if myFunction.check(conn, "Gruppo", "ID", id):

            # Richiedo tutti gli altri campi
            campi = ["Orario", "Anno Accademico", "Tipo Esercitazione", "Matricola Docente", "Programma"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Orario", "Anno_Accademico", "ID_Tipo", "Matricola_Doc", "ID_Pro"]
            myFunction.update(conn, "Gruppo", attributi, valori, "ID = '" + id + "'")

        # Se l'id non esiste scrivo messaggio d'errore
        else:
            print("L'id scelto non esiste")
    if choose == "7":

        # Stampo le partecipazioni, gli studenti e i gruppi
        myFunction.printTable(conn, "SELECT * FROM Studente")
        myFunction.printTable(conn, "SELECT * FROM Gruppo")
        myFunction.printTable(conn, "SELECT * FROM Partecipa")
        print("Selezionare l'id della partecipazione da modificare ", end="")
        id = input()

        # Controllo che l'id inserito esista
        if myFunction.check(conn, "Partecipa", "ID", id):

            # Richiedo tutti gli altri campi
            campi = ["Matricola", "Gruppo"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Matricola_Stud", "ID_Gruppo"]
            myFunction.update(conn, "Partecipa", attributi, valori, "ID = '" + id + "'")

        # Se l'id non esiste scrivo messaggio d'errore
        else:
            print("L'id scelto non esiste")
    if choose == "8":
        os.system("cls")

# Menù Ricerca
if choose == "5":
    print("   MENU RICERCA ")
    print(30 * '-')
    print("1. Visualizza gli esami sostenuti da uno studente")
    print("2. Visualizza la media degli esami sostenuti da uno studente in un gruppo")
    print("3. Visualizza i gruppi gestiti da un docente")
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
        myFunction.printTable(conn, "SELECT * FROM Studente")
        print("Selezionare la matricola dello studente ", end="")
        matricola = input()

        # Controllo che la matricola inserita esista ed eseguo la query
        if myFunction.check(conn, "Studente", "Matricola", matricola):

            query = "SELECT S.Matricola, S.Nome, S.Cognome, E.ID, E.Voto, E.Lode, E.Tipo, E.Data FROM Studente S " \
                    "INNER JOIN Esame E ON S.Matricola = E.Matricola_Stud"
            myFunction.printTable(conn, query)

        # Se la matricola non esiste scrivo messaggio d'errore
        else:
            print("La matricola scelta non esiste")
    if choose == "2":

        # Chiedo la matricola in input
        myFunction.printTable(conn, "SELECT * FROM Studente")
        myFunction.printTable(conn, "SELECT * FROM Partecipa")
        myFunction.printTable(conn, "SELECT * FROM Gruppo")
        print("Selezionare la matricola dello studente ", end="")
        matricola = input()
        print("Selezionare il gruppo di esercitazioni ", end="")
        id = input()

        # Controllo che la matricola inserita esista ed eseguo la query
        if myFunction.check(conn, "Studente", "Matricola", matricola) and myFunction.check(conn, "Gruppo", "ID", id):

            query = "SELECT AVG(E.Voto) AS Media FROM Studente S " \
                    "INNER JOIN Esame E ON S.Matricola = E.Matricola_Stud " \
                    "INNER JOIN Gruppo G ON G.ID = E.ID_Gruppo"
            myFunction.printTable(conn, query)

        # Se la matricola non esiste scrivo messaggio d'errore
        else:
            print("La matricola scelta non esiste")
    if choose == "3":

        # Chiedo l'id in input
        myFunction.printTable(conn, "Esame")
        print("Selezionare l'id da modificare ", end="")
        id = input()

        # Controllo che l'id inserito esista
        if myFunction.check(conn, "Esame", "ID", id):

            # Richiedo tutti gli altri campi
            campi = ["Voto", "Lode", "Data", "Matricola"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Voto", "Lode", "Data", "Matricola_Stud"]
            myFunction.update(conn, "Esame", attributi, valori, "ID = '" + id + "'")

        # Se l'id non esiste scrivo messaggio d'errore
        else:
            print("L'id scelto non esiste")
    if choose == "4":

        # Chiedo l'id in input
        myFunction.printTable(conn, "Tipo")
        print("Selezionare l'id da modificare ", end="")
        id = input()

        # Controllo che l'id inserito esista
        if myFunction.check(conn, "Tipo", "ID", id):

            # Richiedo tutti gli altri campi
            campi = ["Tipo", "Frontale"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Tipo", "Frontale"]
            myFunction.update(conn, "Tipo", attributi, valori, "ID = '" + id + "'")

        # Se l'id non esiste scrivo messaggio d'errore
        else:
            print("L'id scelto non esiste")
    if choose == "5":

        # Chiedo l'id in input
        myFunction.printTable(conn, "Programma")
        print("Selezionare l'id da modificare ", end="")
        id = input()

        # Controllo che l'id inserito esista
        if myFunction.check(conn, "Programma", "ID", id):

            # Richiedo tutti gli altri campi
            campi = ["Descrizione", "Bibliografia"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Descrizione", "Bibliografia"]
            myFunction.update(conn, "Programma", attributi, valori, "ID = '" + id + "'")

        # Se l'id non esiste scrivo messaggio d'errore
        else:
            print("L'id scelto non esiste")
    if choose == "6":

        # Stampo i gruppi, i docenti, i tipi di esercitazione e i programmi d'esame
        myFunction.printTable(conn, "Docente")
        myFunction.printTable(conn, "Tipo")
        myFunction.printTable(conn, "Programma")
        myFunction.printTable(conn, "Gruppo")
        print("Selezionare l'id del gruppo da modificare ", end="")
        id = input()

        # Controllo che l'id inserito esista
        if myFunction.check(conn, "Gruppo", "ID", id):

            # Richiedo tutti gli altri campi
            campi = ["Orario", "Anno Accademico", "Tipo Esercitazione", "Matricola Docente", "Programma"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Orario", "Anno_Accademico", "ID_Tipo", "Matricola_Doc", "ID_Pro"]
            myFunction.update(conn, "Gruppo", attributi, valori, "ID = '" + id + "'")

        # Se l'id non esiste scrivo messaggio d'errore
        else:
            print("L'id scelto non esiste")
    if choose == "7":

        # Stampo le partecipazioni, gli studenti e i gruppi
        myFunction.printTable(conn, "Studente")
        myFunction.printTable(conn, "Gruppo")
        myFunction.printTable(conn, "Partecipa")
        print("Selezionare l'id della partecipazione da modificare ", end="")
        id = input()

        # Controllo che l'id inserito esista
        if myFunction.check(conn, "Partecipa", "ID", id):

            # Richiedo tutti gli altri campi
            campi = ["Matricola", "Gruppo"]
            valori = []
            for n in campi:
                print(n + " = ", end="")
                temp = input()
                while len(temp) == 0:
                    print(n + " = ", end="")
                    temp = input()
                valori.append(temp)

            # Eseguo la funzione di aggiornamento
            attributi = ["Matricola_Stud", "ID_Gruppo"]
            myFunction.update(conn, "Partecipa", attributi, valori, "ID = '" + id + "'")

        # Se l'id non esiste scrivo messaggio d'errore
        else:
            print("L'id scelto non esiste")
    if choose == "8":
        os.system("cls")

# Chiusura della connessione
conn.close()
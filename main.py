import pyodbc
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
if choose == 1:
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
    if choose == 1:

        # Stampo i docenti già presenti
        myFunction.printTable(conn, "Docente")

        # Richiedo i dati e li preparo per la query
        campi = ["Nome", "Cognome", "Indirizzo", "Cap", "Tel", "Data di nascita", "Dipartimento"]
        for n in campi:
            print(n + " = ", end="")
            temp = input()
            valori = "'" + temp +"', "
        valori = valori[:-2]

        # Eseguo la query di inserimento
        attributi = "Nome, Cognome, Indirizzo, Cap, Tel, Data di nascita, Dipartimento"
        myFunction.insertInto(conn, "Docente", attributi, valori)

# Chiusura della connessione
conn.close()
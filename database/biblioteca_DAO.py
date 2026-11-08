from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    # funzione che recupera tutte le biblioteche dal database
    def get_biblioteche(self):
        connessione = DBConnect.get_connection()
        biblioteche = []

        # se la connessione  al database fallisce, restituisce la lista vuota
        if connessione is None:
            return biblioteche

        cursore = connessione.cursor(dictionary = True)
        query = "SELECT * FROM biblioteca" # estrae tutte le colonne da tutte le righe della tabella biblioteca
        cursore.execute(query)

        for riga in cursore:
            biblioteche.append(Biblioteca(**riga)) # **riga --> passa automaticamente tutti i valori estartti dal database alla classe Biblioteca

        cursore.close()
        connessione.close()
        return biblioteche # restitusce la lista di biblioteche da usare nel dropdown

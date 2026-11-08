from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    # funzione che restituisce la lista di tutti i generi presenti nel database
    def get_generi(self):
        # restituisce la lista di tutti i generi
        connessione = DBConnect.get_connection()
        generi = []

        if connessione is None:
            return generi

        cursore = connessione.cursor()
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL"
        cursore.execute(query)

        for riga in cursore:
            generi.append(riga[0])

        cursore.close()
        connessione.close()
        return generi

    def get_libri_filtarti(self, id_biblioteca = None, genere = None):
        # filtra i libri per biblioteca e/o genere
        connessione = DBConnect.get_connection()
        libri_filtrati = []

        if connessione is None:
            return libri_filtrati

        cursore = connessione.cursor(dictionary = True)
        #  COALESCE --> restituisce il primo valore non nullo tra quelli passati come argomento
        query = """
            SELECT * FROM libro
            WHERE (id_biblioteca = COALESCE(%s, id_biblioteca))
              AND (genere = COALESCE(%s, genere))
            ORDER BY titolo
        """
        cursore.execute(query, (id_biblioteca, genere))

        for riga in cursore:
            libri_filtrati.append(Libro(**riga))

        cursore.close()
        connessione.close()
        return libri_filtrati
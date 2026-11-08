import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    # carica le biblioteche
    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        self._view.menu_biblioteca.options.clear()
        self._view.menu_biblioteca.options.append(ft.dropdown.Option(key = "NESSUN_FILTRO", text = "NESSUN FILTRO"))
        for biblioteca in biblioteche:
            self._view.menu_biblioteca.options.append(ft.dropdown.Option(key = str(biblioteca.id), text = biblioteca.nome))

        # carica i generi
        generi = self._model.get_generi()
        self._view.menu_genere.options.clear()
        self._view.menu_genere.options.append(ft.dropdown.Option(key="NESSUN_FILTRO", text="NESSUN FILTRO"))
        for genere in generi:
            self._view.menu_genere.options.append(ft.dropdown.Option(key=genere, text=genere))

        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def gestisci_biblioteca(self, e):
        scelta = self._view.menu_biblioteca.value
        if scelta == "NESSUN_FILTRO" or scelta is None:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(scelta)

    def gestisci_genere(self, e):
        scelta = self._view.menu_genere.value
        if scelta == "NESSUN_FILTRO" or scelta is None:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = scelta

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self, e):
        # pulisce i risultati precedenti
        self._view.lista_libri.controls.clear()

        libri = self._model.get_libri_filtrati(biblioteca = self.biblioteca_selezionata, genere = self.genere_selezionato)

        # se i libri non vengono trovati
        if not libri:
            self._view.show_alert("Nessun libro soddisfa i criteri di ricerca")
            self._view.update()
            return

        for libro in libri:
            testo_libro = f"{libro.titolo} - {libro.autore} ({libro.genere})"
            self._view.lista_libri.controls.append(ft.Text(testo_libro))

        self._view.update()
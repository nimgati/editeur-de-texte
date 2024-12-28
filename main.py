import tkinter

import customtkinter
import customtkinter as ctk
import utils

import json

"""
but du projet :
refaire le notepad de windows en python avec custom tkinter 
 + theme sombre
"""

with open("config.json") as f:
    json_data = json.load(f)

FONT = json_data["font"]

SIZE = json_data["size"]

customtkinter.set_appearance_mode(json_data["theme"])

customtkinter.set_appearance_mode("green")


class editor:
    def __init__(self, file: str = "Sans titre"):
        self.root = utils.default_root.generate_root((950, 600), "Editor", resizable=(False, False))
        self.root.iconbitmap('icone_editor.ico')

        self.menu = tkinter.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file = file

        self.text = ctk.CTkTextbox(self.root, width=950, height=600, font=(FONT, SIZE))
        self.text.pack()

        if file != "Sans titre":
            try:
                self.text.insert("1.0", open(file).read())
            except FileNotFoundError:
                tkinter.messagebox.showerror("ERROR", "Le fichier n'existe pas !")

        self.menu_fichier = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Fichier", menu=self.menu_fichier)
        self.menu_fichier.add_command(label="Nouveau", command=self.nouveau)
        self.menu_fichier.add_command(label="Enregistrer", command=self.enregistrer)
        self.menu_fichier.add_command(label="Enregistrer sous", command=self.enregistrer_sous)
        self.menu_fichier.add_separator()
        self.menu_fichier.add_command(label="Quitter", command=self.root.destroy)

        self.menu_edition = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edition", menu=self.menu_edition)
        self.menu_edition.add_command(label="Copier", command=self.copier)
        self.menu_edition.add_command(label="Couper", command=self.couper)
        self.menu_edition.add_command(label="Coller", command=self.coller)
        self.menu_edition.add_separator()
        self.menu_edition.add_command(label="Rechercher", command=self.rechercher)
        self.menu_edition.add_command(label="Rechercher avec OperaGX", command=self.rechercher_opera)
        self.menu_edition.add_separator()
        self.menu_edition.add_command(label="Remplacer", command=self.remplacer)
        self.menu_edition.add_separator()
        self.menu_edition.add_command(label="Supprimer", command=self.supprimer)

        self.menu_aide = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Aide", menu=self.menu_aide)
        self.menu_aide.add_command(label="A propos", command=self.a_propos)

        self.menu_theme = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Thème", menu=self.menu_theme)
        self.menu_theme.add_command(label="Sombre", command=lambda: customtkinter.set_appearance_mode("dark"))
        self.menu_theme.add_command(label="Clair", command=lambda: customtkinter.set_appearance_mode("light"))
        self.menu_theme.add_command(label="System", command=lambda: customtkinter.set_appearance_mode("system"))

        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        self.root.title(self.file)

        self.root.mainloop()

    def nouveau(self):
        pass

    def enregistrer(self):
        pass

    def enregistrer_sous(self):
        pass

    def copier(self):
        pass

    def couper(self):
        pass

    def coller(self):
        pass

    def rechercher(self):
        pass

    def rechercher_opera(self):
        pass

    def remplacer(self):
        pass

    def supprimer(self):
        pass

    def a_propos(self):
        pass


if __name__ == '__main__':
    editor()

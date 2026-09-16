# -*- coding: utf-8 -*-

"""
Classe ListJury
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass, field

from .jury_chair import JuryChair

# pour éviter une circularité des imports à l'exécution,
# les classes Jury et Book important la classe ListJury
if TYPE_CHECKING:
    from .jury import Jury
    from .book import Book


@dataclass
class ListJury:
    list_jury: list[Jury]
    list_book_selected: list[Book] = field(default_factory=list, init=True)

    def index_jury_chair(self) -> int:
        for jury in self.list_jury:
            if isinstance(jury, JuryChair):
                return self.list_jury.index(jury)

        return -1

    def display_all_books(self) -> None:
        """Affichage de la liste des livres avec pour chacun d'eux :
        - l'id
        - le titre du livre
        - leur auteur
        - l'éditeur"""
        print("[id]: Livre")
        for book in self.list_book_selected:
            print(f"[{book.get_id}]: {book}")

    @staticmethod
    def get_all_book_id_selected(list_book):
        list_id_book = []
        for book in list_book:
            list_id_book.append(str(book.get_id))

        return list_id_book

    def run_votes(self):
        for jury in self.list_jury:
            print(f"Bonjour {jury.first_name} {jury.last_name}.\n"
                  f"Voici la liste des courses en liste")
            self.display_all_books()

            jury.vote(self.list_book_selected)

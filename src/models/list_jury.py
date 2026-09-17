# -*- coding: utf-8 -*-

"""
Classe ListJury
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass, field

from daos import book_dao
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

    NB_TURN: int = 1

    def jury_chair(self) -> JuryChair | None:
        for jury in self.list_jury:
            if isinstance(jury, JuryChair):
                return jury

        return None

    def display_all_books(self) -> None:
        """Affichage de la liste des livres avec pour chacun d'eux :
        - l'id
        - le titre du livre
        - leur auteur
        - l'éditeur"""
        print("[id]: Livre")
        for book in self.list_book_selected:
            print(f"[{book.get_id}]: {book}")

    def run_votes(self):
        while len(self.list_book_selected) != 1:
            for jury in self.list_jury:
                print(f"Bonjour {jury.first_name} {jury.last_name}.\n"
                      f"Voici la liste des livres en liste")
                self.display_all_books()

                jury.vote(self.list_book_selected)

            jury_chairman: JuryChair | None = self.jury_chair()

            if jury_chairman is not None:
                self.list_book_selected = jury_chairman.end_vote(self.list_book_selected, self.NB_TURN)

            self.end_turn()

    def end_turn(self):
        self.NB_TURN += 1
        print(f"==================================\n"
              f"Voici les livres sélectionner au tour {self.NB_TURN}\n"
              f"===================================")

        for book in self.list_book_selected:
            if book is not None:
                book.selected_to_nb_turn = self.NB_TURN
                print(book)
                book_dao.BookDao().update(book)

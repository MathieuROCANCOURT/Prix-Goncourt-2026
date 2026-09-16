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

    def run_votes(self):
        for jury in self.list_jury:
            print(f"Bonjour {jury.first_name} {jury.last_name}.\n"
                  f"Voici la liste des courses en liste")
            self.display_all_books()

            jury.vote(self.list_book_selected)

        jury_chairman: JuryChair | None = self.jury_chair()

        list_id_book_next_turn = []
        if jury_chairman is not None:
            list_id_book_next_turn = jury_chairman.end_vote()

        self.end_turn(list_id_book_next_turn)

    def end_turn(self, list_id_book: list[int]):
        self.list_book_selected = []

        for id_book in list_id_book:
            book: Book | None = book_dao.BookDao().read(id_book)
            if book is not None:
                self.list_book_selected.append(book)
                book.selected_to_nb_turn += 1
                print(book)
                book_dao.BookDao().update(book)

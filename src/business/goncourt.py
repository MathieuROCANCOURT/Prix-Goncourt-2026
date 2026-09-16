# -*- coding: utf-8 -*-

"""
Classe School
"""

from dataclasses import dataclass, field

from daos import book_dao, jury_dao
from models.book import Book
from models.jury import Jury
from models.jury_chair import JuryChair
from models.list_jury import ListJury


@dataclass
class Goncourt:
    list_book: list[Book] = field(default_factory=list, init=True)
    list_jury: list[Jury] = field(default_factory=list, init=True)

    def read_all_book_from_dao(self):
        self.list_book = book_dao.BookDao().read_all()

    def read_all_jury_from_dao(self):
        self.list_jury = jury_dao.JuryDao().read_all()

    def display_book_list(self) -> None:
        """Affichage de la liste des livres avec pour chacun d'eux :
        - leur auteur
        - l'éditeur"""
        for book in self.list_book:
            print(book)

    def init_static(self) -> None:
        """Initialisation d'un jeu de test pour le prix Goncourt."""
        self.read_all_book_from_dao()

        assert len(self.list_book) == 16
        assert self.list_book[0].price == float(format(23.00, ".2f"))
        assert self.list_book[12].author.first_name == "Olivier"

        self.read_all_jury_from_dao()

        assert len(self.list_jury) == 10
        assert isinstance(self.list_jury[0], JuryChair)

        for jury in self.list_jury[1:]:
            assert not isinstance(jury, JuryChair)
            assert isinstance(jury, Jury)

    def init_app(self) -> None:
        list_jury = ListJury(self.list_jury, self.list_book)
        assert list_jury.index_jury_chair() == 0

        list_jury.display_all_books()

# -*- coding: utf-8 -*-

"""
Classe School
"""

from dataclasses import dataclass, field

from models.book import Book


@dataclass
class Goncourt:
    books: list[Book] = field(default_factory=list, init=True)

    def read_all_book_from_dao(self):
        self.books = book_dao.BookDao().read_all()

    def display_book_list(self) -> None:
        """Affichage de la liste des livres avec pour chacun d'eux :
        - leur auteur
        - l'éditeur"""
        for book in self.books:
            print(book)

    def init_static(self) -> None:
        """Initialisation d'un jeu de test pour le prix Goncourt."""

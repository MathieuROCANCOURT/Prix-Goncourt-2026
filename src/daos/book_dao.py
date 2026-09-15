# -*- coding: utf-8 -*-

"""
Classe Dao[Book]
"""
from models.book import Book
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.author import Author
from models.jury import Jury


@dataclass
class BookDao(Dao[Book]):
    def create(self, book: Book) -> int:
        """Crée en BD l'entité Book correspondant au livre Book

        :param book: à créer sous forme d'entité Book en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """

        with Dao.connection.cursor() as cursor:
            return cursor.lastrowid

    def read(self, id_book: int) -> Optional[Book]:
        """Renvoit le livre correspondant à l'entité dont l'id est id_book
           (ou None s'il n'a pu être trouvé)"""
        book: Optional[Book]

        with Dao.connection.cursor():
            return None

    def update(self, book: Book) -> bool:
        """Met à jour en BD l'entité Book correspondant à book, pour y correspondre

        :param book: livre déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            return cursor.rowcount > 0

    def delete(self, book: Book) -> bool:
        pass  # No necessary to delete a book.

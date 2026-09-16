# -*- coding: utf-8 -*-

"""
Classe Dao[Book]
"""
from daos.author_dao import AuthorDao
from daos.editor_dao import EditorDao
from models.book import Book
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any

from models.author import Author
from models.editor import Editor
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

    @staticmethod
    def book_from_db(record: dict[str, Any]) -> Book | None:
        author: Author | None = AuthorDao().read(record["bo_id_author"])
        editor: Editor | None = EditorDao().read(record["bo_id_editor"])

        if author is not None and editor is not None:
            book: Book = Book(record["bo_title"],
                              record["bo_isbn"],
                              record["bo_resume"],
                              record["bo_publication_date"],
                              record["bo_nb_pages"],
                              record["bo_editor_price"],
                              author,
                              editor,
                              record["bo_selected_to_turn"]
                              )
            book.id = record["bo_id_book"]
            return book

        return None

    def read(self, id_book: int) -> Optional[Book]:
        """Renvoit le livre correspondant à l'entité dont l'id est id_book
           (ou None s'il n'a pu être trouvé)"""
        book: Optional[Book] = None

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT * FROM book
                WHERE bo_id_book = %s;
                """
            cursor.execute(sql, (id_book, ))
            record: dict[str, Any] | tuple[Any] | None = cursor.fetchone()

            if isinstance(record, dict):
                book = self.book_from_db(record)

            return book

    def read_all(self) -> list[Book]:
        list_book: list[Book] = []

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT * FROM book;
                """
            cursor.execute(sql)
            records: tuple[dict[str, Any]] | tuple[tuple[Any], ...] | None = cursor.fetchall()

            if records is None:
                return list_book

            for record in records:
                if isinstance(record, dict):
                    book = self.book_from_db(record)
                    if book is not None:
                        list_book.append(book)

            return list_book

    def update(self, book: Book) -> bool:
        """Met à jour en BD l'entité Book correspondant à book, pour y correspondre

        :param book: livre déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            return cursor.rowcount > 0

    def delete(self, book: Book) -> bool:
        pass  # No necessary to delete a book.

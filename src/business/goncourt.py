# -*- coding: utf-8 -*-

"""
Classe School
"""
import datetime
from dataclasses import dataclass, field

from daos import book_dao, jury_dao, author_dao, editor_dao
from models.author import Author
from models.book import Book
from models.editor import Editor
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
        author = Author("Test", "Coucou")
        editor = Editor("Roger Ulula")
        book = Book("test", "1234567890123", "Zut!", datetime.date(2025, 6, 12), 324, 130.25, author, editor)
        jury = Jury("Sam", "Bonbon")
        jury_chair = JuryChair("Albator", "Love")

        # Test create, read and delete Author in Database
        author.id = author_dao.AuthorDao().create(author)

        assert author == author_dao.AuthorDao().read(author.id)

        author_dao.AuthorDao().delete(author)
        assert author_dao.AuthorDao().read(author.id) is None

        # Test create, read and delete Author in Database
        editor.id = editor_dao.EditorDao().create(editor)

        assert editor == editor_dao.EditorDao().read(editor.id)

        editor_dao.EditorDao().delete(editor)
        assert editor_dao.EditorDao().read(editor.id) is None

        book._id = book_dao.BookDao().create(book)

        assert book == book_dao.BookDao().read(book.get_id)
        assert book.author == author_dao.AuthorDao().read(book.author.id)
        assert book.editor == editor_dao.EditorDao().read(book.editor.id)

        book_dao.BookDao().delete(book)

        assert book_dao.BookDao().read(book.get_id) is None
        assert author_dao.AuthorDao().read(book.author.id) is None
        assert editor_dao.EditorDao().read(book.editor.id) is None

        jury.id = jury_dao.JuryDao().create(jury)
        jury_chair.id = jury_dao.JuryDao().create(jury_chair)

        assert jury == jury_dao.JuryDao().read(jury.id)
        assert jury_chair == jury_dao.JuryDao().read(jury_chair.id)
        assert isinstance(jury_dao.JuryDao().read(jury.id), Jury)
        assert isinstance(jury_dao.JuryDao().read(jury_chair.id), JuryChair)

        jury_dao.JuryDao().delete(jury)
        jury_dao.JuryDao().delete(jury_chair)

        assert jury_dao.JuryDao().read(jury.id) is None
        assert jury_dao.JuryDao().read(jury_chair.id) is None

        book_dao.BookDao().reset_book_to_first_turn()
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
        list_jury.run_votes()

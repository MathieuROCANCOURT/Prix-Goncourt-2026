# -*- coding: utf-8 -*-

"""
Classe Jury
"""

from dataclasses import dataclass, field
from typing import Optional

from daos import book_dao
from daos import jury_dao
from .book import Book
from .person import Person


@dataclass
class Jury(Person):
    id: Optional[int] = field(default=None, init=False)
    voted_id_book: Optional[int] = field(default=None, init=False)

    @staticmethod
    def get_all_book_id_selected(list_book):
        list_id_book = []
        for book in list_book:
            list_id_book.append(str(book.get_id))

        return list_id_book

    def vote(self, list_book):
        vote_confirm: bool = False

        while not vote_confirm:
            id_book_vote: str = input("Pour quelle livre voulez-vous voter (en saisissant l'id) ?")

            while id_book_vote not in self.get_all_book_id_selected(list_book):
                id_book_vote = input("Vous n'avez pas saisie de choix parmi la liste des livre.\nVeuillez réessayer.")

            book_vote: Book | None = book_dao.BookDao().read(int(id_book_vote))
            print(f"Voici le livre que vous avez choisi: {book_vote}")
            response_confirm = input("Voulez-vous confirmez votre choix ? [Y/n]")

            if response_confirm == "" or response_confirm.lower() == 'y':
                self.voted_id_book = int(id_book_vote)
                vote_confirm = True
                jury_dao.JuryDao().update_vote(self)

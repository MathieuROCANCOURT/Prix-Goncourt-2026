# -*- coding: utf-8 -*-

"""
Classe JuryChair
"""

from dataclasses import dataclass

from daos import jury_dao, book_dao
from .book import Book
from .jury import Jury


@dataclass
class JuryChair(Jury):
    @staticmethod
    def vote_counts_twice(is_draw: bool) -> int:
        return 2

    def end_vote(self, list_book, nb_actual_turn):
        result = jury_dao.JuryDao().count_vote()
        print("Voici les résultats du vote:")

        list_book, list_id_book = self.display_result(result, list_book, nb_actual_turn)

        if len(list_id_book) > 4:
            list_book.clear()
            list_book_id_next_turn = []

            for _ in range(len(result) // (2 * nb_actual_turn)):
                book, id_selected = self.check_input_id(list_id_book, list_book_id_next_turn)
                list_book.append(book)
                list_book_id_next_turn.append(id_selected)
            return list_book

        return self.last_selection(result, list_book)

    def last_selection(self, result, list_book):
        list_book_next_turn = []
        max_nb_vote = result[0]["count_vote"]

        if max_nb_vote == result[-1]["count_vote"]:
            response = input("Est-ce que le président du jury veut utiliser son double voix ?[Y/n]")
            if response == "" or response.lower() == "y":
                list_book_next_turn.append(self.voted_id_book)
            else:
                return list_book
        else:
            for id_book, nb_vote in result:
                if max_nb_vote == nb_vote:
                    list_book_next_turn.append(book_dao.BookDao().read(id_book))
                else:
                    break
        return list_book_next_turn

    @staticmethod
    def display_result(result, list_book, actual_turn):
        list_id_book = []
        for row in result:
            id_book = row["bo_id_book"]
            book: Book | None = book_dao.BookDao().read(id_book)

            if book is not None and book.selected_to_nb_turn == actual_turn:
                list_book.append(book)
                list_id_book.append(book.get_id)
                print(f"[{book.get_id}] {book}: {row["count_vote"]} voix.")

        return list_book, list_id_book

    @staticmethod
    def check_input_id(list_id_book, list_id_book_next_turn) -> tuple[Book | None, int]:
        id_book_selected = input("Saisir les id du livre qui passe au prochain tour.")

        while (not id_book_selected.isdigit()
               or int(id_book_selected) not in list_id_book
               or int(id_book_selected) in list_id_book_next_turn):
            id_book_selected = input("Saisie Incorrect\nSaisir les id du livre qui passe au prochain tour.")

        return book_dao.BookDao().read(int(id_book_selected)), int(id_book_selected)

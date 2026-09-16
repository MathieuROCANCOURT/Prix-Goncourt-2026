# -*- coding: utf-8 -*-

"""
Classe JuryChair
"""

from dataclasses import dataclass

from daos import jury_dao, book_dao
from .jury import Jury


@dataclass
class JuryChair(Jury):
    @staticmethod
    def vote_counts_twice(is_draw: bool) -> int:
        return 2

    def end_vote(self):
        list_id_book = []
        list_id_book_next_turn = []
        result = jury_dao.JuryDao().count_vote()
        print("Voici les résultats du vote:")

        list_id_book = self.display_result(result, list_id_book)

        if len(result) > 4:
            for _ in range(len(result) // 2):
                list_id_book_next_turn.append(self.check_input_id(list_id_book))
        else:
            max_nb_vote = result[0]["count_vote"]

            if max_nb_vote == result[-1]["count_vote"]:
                input("Est-ce que le président du jury veut utiliser son double voix ?[Y/n]")
                list_id_book_next_turn.append(self.voted_id_book)
            else:
                for id_book, nb_vote in result:
                    if max_nb_vote == nb_vote:
                        list_id_book_next_turn.append(id_book)
                    else:
                        break

        return list_id_book_next_turn

    @staticmethod
    def display_result(result, list_id_book):
        for row in result:
            id_book = row["bo_id_book"]
            list_id_book.append(id_book)
            print(f"[{id_book}] {book_dao.BookDao().read(id_book)}: {row["count_vote"]} voix.")

        return list_id_book

    @staticmethod
    def check_input_id(list_id_book) -> int:
        id_book_selected = input("Saisir les id du livre qui passe au prochain tour.")

        while not id_book_selected.isdigit() or int(id_book_selected) not in list_id_book:
            id_book_selected = input("Saisie Incorrect\nSaisir les id du livre qui passe au prochain tour.")

        return int(id_book_selected)

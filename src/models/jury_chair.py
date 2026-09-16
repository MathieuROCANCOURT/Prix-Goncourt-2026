# -*- coding: utf-8 -*-

"""
Classe JuryChair
"""

from dataclasses import dataclass, field
from .jury import Jury


@dataclass
class JuryChair(Jury):
    @staticmethod
    def vote_counts_twice(is_draw: bool) -> int:
        return 2

    @staticmethod
    def end_vote():
        list_id_book = []
        list_id_book_next_turn = []
        result = jury_dao.JuryDao().count_vote()
        print("Voici les résultats du vote:")

        for row in result:
            id_book = row["bo_id_book"]
            list_id_book.append(id_book)
            print(f"[{id_book}] {book_dao.BookDao().read(id_book)}: {row["count_vote"]} voix.")

        for _ in range(len(result) // 2):
            id_book_selected = input("Saisir les id du livre qui passe au prochain tour.")

            while not id_book_selected.isdigit() or int(id_book_selected) not in list_id_book:
                id_book_selected = input("Saisie Incorrect\nSaisir les id du livre qui passe au prochain tour.")

            list_id_book_next_turn.append(int(id_book_selected))

        return list_id_book_next_turn

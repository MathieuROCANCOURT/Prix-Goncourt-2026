# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""
from daos import editor_dao, book_dao
from models.book import Book
from models.jury import Jury
from models.person import Person
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class Jury(Dao[Jury]):
    def create(self, jury: Jury) -> int:
        """Crée en BD l'entité Jury correspondant à l'adresse jury

        :param jury: à créer sous forme d'entité Jury en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            return cursor.lastrowid

    def read(self, id_jury: int) -> Optional[Jury]:
        """Renvoit le jury correspondant à l'entité dont l'id est ju_id_jury
           (ou None s'il n'a pu être trouvé)"""
        jury: Optional[Jury]

        with Dao.connection.cursor():
            return None

    def update(self, jury: Jury) -> bool:
        """Met à jour en BD l'entité Jury correspondant à jury, pour y correspondre

        :param jury: jury déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            return cursor.rowcount > 0

    def delete(self, jury: Jury) -> bool:
        """Supprime en BD l'entité Jury correspondant à jury

        :param jury: jury dont l'entité Jury correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        pass  # Don't necessary to delete a jury.

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

    @staticmethod
    def jury_from_db(record: dict[str, Any]) -> Jury | None:
        jury: Optional[Jury]

        jury = Jury(record["pe_first_name"],
                    record["pe_last_name"])
        jury.id = record["jury.ju_id_jury"]

        return jury

    def read(self, id_jury: int) -> Optional[Jury]:
        """Renvoit le jury correspondant à l'entité dont l'id est ju_id_jury
           (ou None s'il n'a pu être trouvé)"""
        jury: Optional[Jury]

        with Dao.connection.cursor():
            return None

    def read_all(self) -> list[Jury]:
        list_jury: list[Jury] = []

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT
                    jury.ju_id_jury,
                    ju_is_chairman,
                    pe_first_name,
                    pe_last_name,
                    bo_id_book
                FROM jury
                JOIN person ON person.pe_id_person = ju_id_person
                LEFT JOIN vote ON vote.ju_id_jury = jury.ju_id_jury;
                """
            cursor.execute(sql)
            records: tuple[dict[str, Any]] | tuple[tuple[Any], ...] | None = cursor.fetchall()

            if records is None:
                return list_jury

            for record in records:
                if isinstance(record, dict):
                    jury: Jury | None = self.jury_from_db(record)
                    if jury is not None:
                        list_jury.append(jury)

            return list_jury

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

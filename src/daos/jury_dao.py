# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""
from models.jury import Jury
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any

from models.jury_chair import JuryChair


@dataclass
class JuryDao(Dao[Jury]):
    def create(self, jury: Jury) -> int:
        """Crée en BD l'entité Jury correspondant à l'adresse jury

        :param jury: à créer sous forme d'entité Jury en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                        INSERT INTO person(pe_first_name, pe_last_name)
                        VALUES (%s, %s);
                    """
                cursor.execute(sql, (jury.first_name, jury.last_name))
                id_person = cursor.lastrowid

                if isinstance(jury, JuryChair):
                    sql = """
                            INSERT INTO jury(ju_id_person, ju_is_chairman)
                            VALUES (%s, 1);
                        """
                else:
                    sql = """
                            INSERT INTO jury(ju_id_person, ju_is_chairman)
                            VALUES (%s, 0);
                        """
                cursor.execute(sql, (id_person,))

                return cursor.lastrowid

        except Exception as e:
            print(f"Exception : {e}")

        return -1

    @staticmethod
    def jury_from_db(record: dict[str, Any]) -> Jury | None:
        jury: Optional[Jury]

        if record["ju_is_chairman"] == 1:
            jury = JuryChair(record["pe_first_name"],
                             record["pe_last_name"])
        else:
            jury = Jury(record["pe_first_name"],
                        record["pe_last_name"])
        jury.id = record["ju_id_jury"]
        jury.voted_id_book = record["bo_id_book"]

        return jury

    def read(self, id_jury: int) -> Optional[Jury]:
        """Renvoit le jury correspondant à l'entité dont l'id est ju_id_jury
           (ou None s'il n'a pu être trouvé)"""
        jury: Optional[Jury] = None

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT * FROM jury
                JOIN person ON person.pe_id_person = jury.ju_id_person
                WHERE ju_id_jury = %s;
                """
            cursor.execute(sql, (id_jury,))
            record: dict[str, Any] | tuple[Any] | None = cursor.fetchone()

            if isinstance(record, dict):
                jury = self.jury_from_db(record)

            return jury

    def read_all(self) -> list[Jury]:
        list_jury: list[Jury] = []

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT
                    jury.ju_id_jury,
                    ju_is_chairman,
                    pe_first_name,
                    pe_last_name,
                    ju_id_book
                FROM jury
                JOIN person ON person.pe_id_person = ju_id_person;
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
        try:
            with Dao.connection.cursor() as cursor:
                if isinstance(jury, JuryChair):
                    sql = """
                            UPDATE jury, person
                            SET pe_first_name=%s, pe_last_name=%s, ju_is_chairman=1, ju_id_book=%s
                            WHERE ju_id_jury = %s;
                        """
                else:
                    sql = """
                            UPDATE jury, person
                            SET pe_first_name=%s, pe_last_name=%s, ju_is_chairman=0, ju_id_book=%s
                            WHERE ju_id_jury = %s;
                        """
                cursor.execute(sql, (jury.first_name, jury.last_name, jury.voted_id_book, jury.id))

                return cursor.rowcount > 0

        except Exception as e:
            print(f"Exception : {e}")

        return False

    @staticmethod
    def update_vote(jury: Jury) -> bool:
        """Met à jour en BD l'entité Jury correspondant à jury, pour y correspondre

        :param jury: jury déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        try:
            with Dao.connection.cursor() as cursor:
                if isinstance(jury, JuryChair):
                    sql = """
                            UPDATE jury
                            SET ju_id_book=%s
                            WHERE ju_id_jury = %s;
                        """
                else:
                    sql = """
                            UPDATE jury, person
                            SET ju_id_book=%s
                            WHERE ju_id_jury = %s;
                        """
                cursor.execute(sql, (jury.voted_id_book, jury.id))

                return cursor.rowcount > 0

        except Exception as e:
            print(f"Exception : {e}")

        return False

    @staticmethod
    def count_vote():
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                        SELECT bo_id_book, COUNT(ju_id_book) AS count_vote
                        FROM jury
                        RIGHT JOIN book ON book.bo_id_book = jury.ju_id_book
                        GROUP BY bo_id_book
                        ORDER BY count_vote DESC;
                    """
                cursor.execute(sql)
                return cursor.fetchall()

        except Exception as e:
            print(f"Exception : {e}")

        return []

    def delete(self, jury: Jury) -> bool:
        """Supprime en BD l'entité Jury correspondant à jury

        :param jury: jury dont l'entité Jury correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    DELETE jury, person FROM person
                    JOIN jury ON jury.ju_id_person = person.pe_id_person
                    WHERE jury.ju_id_jury = %s;
                    """
                cursor.execute(sql, (jury.id,))

                return True

        except Exception as e:
            print(f"Exception : {e}")

        return False

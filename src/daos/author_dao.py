# -*- coding: utf-8 -*-

"""
Classe Dao[Author]
"""
from models.author import Author
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class AuthorDao(Dao[Author]):
    def create(self, author: Author) -> int:
        """Crée en BD l'entité Author correspondant au livre author

        :param author: à créer sous forme d'entité Author en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            return cursor.lastrowid > 0

    @staticmethod
    def read_author_from_db(record: dict[str, Any]) -> Author | None:
        author: Optional[Author]

        author = Author(record["pe_first_name"],
                        record["pe_last_name"])
        author.id = record["au_id_author"]
        author.biography = record["au_biography"]

        return author


    def read(self, id_author: int) -> Optional[Author]:
        """Renvoit l'auteur correspondant à l'entité dont l'id est au_id_author
           (ou None s'il n'a pu être trouvé)"""
        with Dao.connection.cursor() as cursor:
            sql = """
                    SELECT au_id_author, pe_first_name, pe_last_name, au_biography FROM author
                    JOIN person ON person.pe_id_person = author.au_id_person
                    WHERE au_id_author = %s;
                """

            cursor.execute(sql, (id_author,))
            record: dict[str, Any] | tuple[Any] | None = cursor.fetchone()

        if isinstance(record, dict):
            return self.read_author_from_db(record)

        return None


    def update(self, author: Author) -> bool:
        """Met à jour en BD l'entité Author correspondant à author, pour y correspondre

        :param author: auteur déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            return cursor.rowcount > 0

    def delete(self, author: Author) -> bool:
        """Supprime en BD l'entité author correspondant à author

        :param author: livre dont l'entité Author correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        pass  # Don't necessary to delete an author.

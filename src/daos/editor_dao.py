# -*- coding: utf-8 -*-

"""
Classe Dao[Editor]
"""
from models.editor import Editor
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class EditorDao(Dao[Editor]):
    def create(self, editor: Editor) -> int:
        """Crée en BD l'entité Editor correspondant à l'éditeur Editor

        :param editor: à créer sous forme d'entité Editor en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql_increment = "ALTER TABLE editor AUTO_INCREMENT = 1;"
                cursor.execute(sql_increment)

                sql = """
                    INSERT INTO editor(ed_name)
                    VALUES (%s);
                    """
                cursor.execute(sql, (editor.name,))

                return cursor.lastrowid

        except Exception as e:
            print(f"Exception : {e}")

        return 0

    def read(self, id_editor: int) -> Optional[Editor]:
        """Renvoit l'éditeur correspondant à l'entité dont l'id est id_editor
           (ou None s'il n'a pu être trouvé)"""
        editor: Optional[Editor] = None

        with Dao.connection.cursor() as cursor:
            sql = """
                    SELECT * FROM editor
                    WHERE ed_id_editor = %s;
                """

            cursor.execute(sql, (id_editor,))
            record: dict[str, Any] | tuple[Any] | None = cursor.fetchone()

        if isinstance(record, dict):
            editor = Editor(record["ed_name"])
            editor.id = record["ed_id_editor"]

        return editor

    def update(self, editor: Editor) -> bool:
        """Met à jour en BD l'entité Editor correspondant à editor, pour y correspondre

        :param editor: éditeur déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                        UPDATE editor
                        SET ed_name = %s
                        WHERE ed_id_editor = %s;
                    """
                cursor.execute(sql, (editor.name, editor.id))

                return cursor.rowcount > 0

        except Exception as e:
            print(f"Exception : {e}")

        return False

    def delete(self, editor: Editor) -> bool:
        """Supprime en BD l'entité Editor correspondant à editor

        :param editor: éditeur dont l'entité Editor correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    DELETE FROM editor
                    WHERE ed_id_editor = %s;
                    """
                cursor.execute(sql, (editor.id,))

                return True

        except Exception as e:
            print(f"Exception : {e}")

        return False

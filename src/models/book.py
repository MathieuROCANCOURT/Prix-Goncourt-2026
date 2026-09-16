# -*- coding: utf-8 -*-

"""
Classe Book
"""

from __future__ import annotations

from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass, field
from datetime import date

# pour éviter une circularité des imports à l'exécution,
# les classes Author et Editor important la classe Book
if TYPE_CHECKING:
    from .author import Author
    from .editor import Editor


@dataclass
class Book:
    id: Optional[int] = field(default=None, init=False)
    title: str
    isbn: str
    resume: str
    publish_date: date
    nb_pages: int
    price: float
    author: Author
    editor: Editor
    list_main_people: list[str] = field(default_factory=list, init=False)
    selected_to_nb_turn: int = 1

    @property
    def get_id(self):
        return self.__id

    def __str__(self) -> str:
        course_str = (f"Le titre est {self.title} écrit par {self.author.__str__()} publier le {self.publish_date}.\n"
                      f"{self.editor.__str__()}")
        return course_str

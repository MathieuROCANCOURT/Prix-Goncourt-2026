# -*- coding: utf-8 -*-

"""
Classe ListJury
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass, field

from .jury_chair import JuryChair

# pour éviter une circularité des imports à l'exécution,
# les classes Jury et Book important la classe ListJury
if TYPE_CHECKING:
    from .jury import Jury
    from .book import Book


@dataclass
class ListJury:
    list_jury: list[Jury]
    list_book_selected: list[Book] = field(default_factory=list, init=True)

    def index_jury_chair(self) -> int:
        for jury in self.list_jury:
            if isinstance(jury, JuryChair):
                return self.list_jury.index(jury)

        return -1

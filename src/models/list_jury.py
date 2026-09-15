# -*- coding: utf-8 -*-

"""
Classe ListJury
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass, field

# pour éviter une circularité des imports à l'exécution,
# les classes Jury, JuryChair et Book important la classe ListJury
if TYPE_CHECKING:
    from .jury import Jury
    from .jury_chair import JuryChair
    from .book import Book


@dataclass
class ListJury:
    jury_chair: JuryChair
    list_jury: list[Jury]
    list_book_selected: list[Book] = field(default_factory=list, init=True)

# -*- coding: utf-8 -*-

"""
Classe Author, fille de la classe Person
"""

from dataclasses import dataclass, field
from typing import Optional
from .person import Person


@dataclass
class Author(Person):
    id: Optional[int] = field(default=None, init=False)
    biography: Optional[str] = field(default=None, init=False)

    def __str__(self) -> str:
        person_str = super().__str__()
        if self.biography is not None:
            person_str += ", Biographie:\n" + self.biography

        return person_str

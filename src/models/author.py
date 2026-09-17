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
        return f"Biographie: {super().__str__()}"

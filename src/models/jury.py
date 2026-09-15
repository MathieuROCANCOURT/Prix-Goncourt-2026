# -*- coding: utf-8 -*-

"""
Classe Jury
"""

from dataclasses import dataclass, field
from typing import Optional
from .person import Person


@dataclass
class Jury(Person):
    id: Optional[int] = field(default=None, init=False)

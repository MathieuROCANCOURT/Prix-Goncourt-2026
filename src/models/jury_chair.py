# -*- coding: utf-8 -*-

"""
Classe JuryChair
"""

from dataclasses import dataclass, field
from typing import Optional
from .person import Person


@dataclass
class JuryChair(Person):
    id: Optional[int] = field(default=None, init=False)

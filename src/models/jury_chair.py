# -*- coding: utf-8 -*-

"""
Classe JuryChair
"""

from dataclasses import dataclass, field
from typing import Optional
from .jury import Jury


@dataclass
class JuryChair(Jury):
    def __init__(self):
        super().__init__()

# -*- coding: utf-8 -*-

"""
Classe JuryChair
"""

from dataclasses import dataclass, field
from .jury import Jury


@dataclass
class JuryChair(Jury):
    @staticmethod
    def vote_counts_twice(is_draw: bool) -> int:
        return 2

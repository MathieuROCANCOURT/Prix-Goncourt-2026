# -*- coding: utf-8 -*-

"""
Classe Editor
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Editor:
    """Adresse d'une personne (enseignant ou élève)."""
    id: Optional[int] = field(default=None, init=False)
    name: str

    def __str__(self) -> str:
        return f"L'éditeur est {self.name}."

# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de Jury, JuryChair et Author
"""

from abc import ABC
from dataclasses import dataclass


@dataclass
class Person(ABC):
    """Personne liée au prix Goncourt : enseignant ou élève."""
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

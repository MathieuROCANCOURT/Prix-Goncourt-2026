#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'un prix Goncourt 2026
"""

from business.goncourt import Goncourt


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans l'élection du prix Goncourt 2026
--------------------------""")

    goncourt: Goncourt = Goncourt()

    # initialisation d'un ensemble de jury, d'auteurs, d'éditeurs et de livres composant le prix Goncourt.
    goncourt.init_static()

    # affichage de la liste des cours, leur éditeur et leur auteur
    goncourt.display_book_list()


if __name__ == '__main__':
    main()

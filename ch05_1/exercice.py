#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
import math

def convert_to_absolute(number: float) -> float:
    number = (number)**2
    number = math.sqrt(number)
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'

    liste = prefixes.replace("", " ")
    liste.split(" ")
    liste = prefixes.replace(" ", "")
    nouveau_nom = []

    for elem in liste:
        nouveau_nom.append(elem + suffixe)


    return nouveau_nom


def prime_integer_summation() -> int:

    num = 1
    somme = 0
    count = 0

    while True:
        if num / num == 1 and num / 1 == num:
            somme += num
            count += 1

        if count == 100:
            break
        
        
        num += 1
    return somme


def factorial(number: int) -> int:
    fact = 1
    for x in range(2, number + 1):
        fact *= x

    return fact


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []
    for group in groups:
        if 25 in group:
            acceptance.append(True)
            continue
        if min(group) < 18:
            acceptance.append(False)
            continue
        if len(group) > 10 and len(group) <= 3:
            acceptance.append(False)
            continue
        if min(group) < 18 or max(group) > 70 and group == 50:
            acceptance.append(False)
            continue
        else:
            acceptance.append(True)
    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()

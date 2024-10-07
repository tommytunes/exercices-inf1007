#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majuscule(mot):
    new_words = ""
    for elem in mot:
        new_words += (chr(ord(elem)-32))
        
    return new_words


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

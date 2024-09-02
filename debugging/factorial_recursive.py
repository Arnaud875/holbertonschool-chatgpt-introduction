#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le factoriel d'un nombre entier n de manière récursive.

    Le factoriel d'un nombre n est défini comme étant le produit de tous les 
    entiers positifs inférieurs ou égaux à n. Par définition, le factoriel de 0 est 1.

    Args:
        n (int): Un entier non négatif dont on veut calculer le factoriel.

    Returns:
        int: Le factoriel de n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Récupère l'argument de la ligne de commande, le convertit en entier, 
# puis calcule et affiche son factoriel.
f = factorial(int(sys.argv[1]))
print(f)

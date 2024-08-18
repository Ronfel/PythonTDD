"""
1 - Receber um número inteiro
2 - Saber se o número é multiplo de 3 e 5:
Bacon com ovos
3 - Saber se o número não é multiplo de 3 e 5:
Passar Fome
4 - Saber se o número é multiplo de 3:
Bacon
5 - Saber se o número é multiplo de 5:
Ovos

"""

def bacon_com_ovos(n):
    assert isinstance(n, int), "'n' deve ser inteiro."
    

    if n % 3 == 0 and n % 5 == 0:
        return "Bacon com ovos"
    elif n % 3 != 0 and n % 5 != 0:
        return "Passar Fome"
    elif n % 3 == 0:
        return "Bacon"
    elif n % 5 == 0:
        return "Ovos"
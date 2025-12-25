"""
try:
    numInt = int(input("digite um numro inteiro "))
    
    resultado = numInt % 2
    if resultado == 0:
        print("seu numero é par")
    else:
        print("seu numero é ímpar")
     
except ValueError:
    print("digite apenas numeros inteiro")
    print(ValueError)
"""

"""
try:
    hora = float(input("qual é a hora 'apenas numeros': "))
    if hora >= 0 and hora <= 11:
        print("bom dia")
    elif hora >= 12 and hora <= 17:
        print("boa tarde")
    else:
        print("boa noite")
except ValueError:
    print(f"digite apenas numeros.\nvalor do erro: {ValueError}")
"""

"""
nome = input("qual o seu nome? ")

if len(nome) <= 4:
    print("seu nome é curto")
elif len(nome) <= 6:
    print("seu nome é normal")
elif len(nome) > 6:
    print("seu nome é grande")
"""



    
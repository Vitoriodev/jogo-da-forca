texto = input("escrevar seu nome: ")

indice = 0
novo_texto = ""
while True:
    
    valor_texto = len(texto)
    if valor_texto > indice:
        
        print(f"*{texto[indice]}*")
        letra = texto[indice]
        novo_texto += letra
        
        indice += 1
    else:
        print(novo_texto)
        break
        
    
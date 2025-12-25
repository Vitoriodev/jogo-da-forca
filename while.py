texto = input("escrevar um texto")

#essa logica que eu fiz no while o for ja faz sozinho 

"""i = 0
texto_meno = 0
guarda_texto = ""

while i < len(texto):
    texto_atual = texto[i] #aqui vai pegar uma letra por vez
    
    if texto_atual == " ": #vai tiras os espaços 
        i += 1
        continue
    
    texto_repetido = texto.count(texto_atual) #vai guarda quantas vezes a letra apareceu no texto
    
    if texto_meno < texto_repetido: #aqui vai guarda a maior letra que aparecer mais vezes
        texto_meno = texto_repetido
        guarda_texto = texto_atual
        
    i += 1"""
    
for letra in texto:
    print(letra)
    

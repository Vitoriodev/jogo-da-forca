import getpass # uma libre que posso esconder o que  o usuario está digitando.
import time # uma libre de tempo.
import os # uma libre de sistema.

# autor @vitorio.

# função de limpar o terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# caregamento de 4 segundos
def contagem_de_pontos():
    i = 0
    print("caregando", end="")
    while True:
        print(".", end="", flush=True)
        # o flush vai foça o "." aparecer no print um por um e não de uma vez só.
        time.sleep(1)
        i += 1
        if i == 4:
            print()
            break
        
# vai está começando limpando o terminal
limpar_tela()
while True:
    # não mostra a palavra sendo escrita usando o getpass.
    palavra = getpass.getpass("digite a palavra que vai ser advinhadar: ")

    print(f"essa e a palavra que você escolheu: {palavra}")
    contagem_de_pontos()
    limpar_tela()
    
    op = input("está tudo certo com a palavra s/n: ").lower()
        
    # ser o usuario não gostou da palavra que ela escolheu ela poder voltar para escrever novamente.
    if op == "n":
        print("você vai ser direcionado novamente para adiciona uma nova palavra")
        contagem_de_pontos()
        limpar_tela()
        continue
    
    palavra_secreta = ["_" for letra in palavra] # vai criar uma lista que vai colocar uma _ para pode subistituir depois.
    
    # 
    vida = 6 # vida do usuario se ele perder todas as vidas ele perde.
    print("total de letra")
    print(" _ " *len(palavra))
    
    while True:
        
        print(f"vidas restante: {vida}")
        letra_usuario = input("digite uma letra: ").lower()
        acertou_a_rodada = False
        # vai fazer uma verificação ser a palavra 
        j = 0
        for i in palavra:
            if letra_usuario == i:
                palavra_secreta[j] = letra_usuario
                acertou_a_rodada = True
            j += 1
        
        limpar_tela()
        print(*palavra_secreta) # vai mostra os acertos das letras.
        
        # quando o jogador não acertar uma letra vai perder uma vida
        if not acertou_a_rodada:
            vida -= 1
            
        # se o jogador zera a vida vai fechar o loop         
        if vida == 0:
            print("==" *20)
            print(f"você perdeu o jogo! \nessa era a palavra secreta: {palavra}")
            print("==" *20)
            break
        # vai verifica se o jogado terminou de escrever a palavra secreta.
        if "_" not in palavra_secreta:
            print("==" *20)
            print(f"parabéns essa é a certa: {palavra}")
            print("==" *20)
            break
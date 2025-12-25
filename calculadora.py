import os

try:
    print("CALCULADORA")
    while True:
        
        #opção de fechar o loop
        sair = input("quer fechar a calculadora? s/n: ").upper()
        if sair == "S" or sair == "N":
            if sair == "S": #Ser o usuario não digitar S a calculadora não vai fechar e vai continuar normalmente.
                os.system('clear')
                print("fechando calculadora...")
                break
        else:
            os.system('clear')
            print("digiter apenas 'S' ou 'N'")
            continue
        
        print("qual opção vai escolher 1= + 2= - 3= / 4= *")
        op = int(input("escohlhar a opção: "))
        os.system('clear')
        
        if op == 1: #soma
            print("-------------------")
            num = float(input("primeiro numero: "))
            num2 = float(input("segundo numero: "))
            total = num + num2
            print(f"{num} + {num2} = {total:.2f}")
            print("-------------------")
            
        elif op == 2: #subtração
            print("-------------------")
            num = float(input("primeiro numero: "))
            num2 = float(input("segundo numero: "))
            total = num - num2
            print(f"{num} - {num2} = {total:.2f}")
            print("-------------------")
            
        elif op == 3: # divisão
            print("-------------------")
            num = float(input("primeiro numero: "))
            num2 = float(input("segundo numero: "))
            if num2 == 0:
                print("não é possivel dividir um numero por zero")
                print("-------------------")
                continue
            total = num / num2
            print(f"{num} / {num2} = {total:.2f}")
            print("-------------------")
            
        elif op == 4: #multiplicação    
            print("-------------------")
            num = float(input("primeiro numero: "))
            num2 = float(input("segundo numero: "))
            total = num * num2
            print(f"{num} * {num2} = {total:.2f}")
            print("-------------------")
        else:
            os.system('clear')
            print("-------------------")
            print("essa opção não exister")
            print("-------------------")

except ValueError:
    print(f"ERRO {ValueError}")
    
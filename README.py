menu = ()
[d] Depositar
[s] Sacar 
[e] Extrato 
[q] Sair


saldo = 0 
limite = 500 
numero_saques = 0
LIMITE_SAQUE = 3

while True: 
    opcao = input (menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0
        saldo += valor 
        extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
        print("Operação falhou! O Valor informado é inválido")
   
    
    elif opcao == "s":
    valor = float(input("Informe o valor do saque:"))

    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUE  

    if excedeu saldo:
    print("Operação falhou! Você não tem saldo suficiente!")

    elif excedeu_limite:
    print("Operação falhou, o valor excede o limite")

    elif excedeu_saques:
    print("Operação falhou! Você atingiu o número de saque diário!")

    elif valor > 0:
    saldo -= valor
    extrato += f"Saque: R${valor:.2f}\n"
    numero_saques +=1 

    else:
    print("Operação falhou! O Valor informado é inválido")
    
    elif opcao == "e":
        print("\n====================== Extrato ======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\nSaldo: R${saldo:.2f}") 
        print ("================================")

    
    elif opcao == "q": 
        break 
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")

    


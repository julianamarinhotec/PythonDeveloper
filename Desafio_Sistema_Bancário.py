menu = """

======= Olá! Bem vindo ao BJM. =======

Como o BJM pode te ajudar?
Escolha uma das opções:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
valor = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if  valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
                
        else:
            print("Falha na operação. O valor informado é inválido.")
    
    elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= limite_saques

            if excedeu_saldo:
                print("Falha na operação. Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Faha na operação. O valor do saque ultrapassa o limite.")

            elif excedeu_saques:
                print("Falha na operação. Número máximo de saques atingido.")
         
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Falha na operação. O valor informado é inválido.")

    elif opcao == "e":
        print("\n ============== Extrato =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}\n")
        print("\nOperação finalizada com sucesso.")
        print("\nAbraços equipe BJM.")
        print("===================================")
        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    


         
         


    
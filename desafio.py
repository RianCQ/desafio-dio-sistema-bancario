menu = """
----- Menu -----
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [nc] Nova conta
  [nu] Novo usuário
  [p] Parar

  => """
'''
saldo = 0
limite = 500
limite_saques = 3
numero_saques = 0
depositos = []
#saques = []
'''

def depositar(saldo, valor, extrato, /):
    if valor > 0.0:
        saldo = saldo + valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("Deposito realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > 0:
        if numero_saques < limite_saques :
            if valor <= limite:
                if saldo > valor :
                    saldo = saldo - valor
                    extrato += f"Saque: R${valor:.2f}\n"
                    numero_saques += 1
                    print("Saque realizado com sucesso.")
                else :
                    print("Erro: Saldo insuficiente.")
            else:
                print("Erro: Valor de saldo excede o limite de retirada.")
        else:
            print("Erro: Limite de saques diários atingido.")
    else:
        print("Erro: Valor de saque inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato) -> None:
    print("################ Extrato ##################")
    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")
    else :
        print(extrato)
        print()
        print(f"> Saldo total: R${saldo:.2f}")
    print("###########################################")

def main():
    LIMITE_SAQUES = 3
    #AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == 'd':
            valor = float(input("Qual o valor de deposito? "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 's':
            valor = float(input("Qual o valor de saque? "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 'p':
            print("Saindo do processo...")
            break
        else:
            print("Erro: Operação inválida. Por favor, selecione novamente a operação desejada.")

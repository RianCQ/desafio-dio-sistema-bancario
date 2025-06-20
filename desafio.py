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

def deposito(saldo: float, valor: float, depositos: list):
    if valor > 0.0:
        saldo = saldo + valor
        depositos.append(valor)
        print("Deposito realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")
    return saldo

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
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
    return saldo

def extrato(saldo: float, depositos, saques: list) -> None:
    print("################ Extrato ##################")
    if len(depositos) == 0 and len(saques) == 0:
        print("Não foram realizadas movimentações.")
    else :
        indice = 0
        print("> Depósitos: ")
        while indice < len(depositos):
            print(f"R${depositos[indice]:.2f}")
            indice += 1
        print()
        indice = 0
        print("> Saques: ")
        while indice < len(saques):
            print(f"R${saques[indice]:.2f}")
            indice += 1
        print()
        print(f"> Saldo total: R${saldo:.2f}")
    print("###########################################")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

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
            saldo = deposito(saldo, valor, depositos)
        elif opcao == 's':
            valor = float(input("Qual o valor de saque? "))
            saldo = saque(saldo=saldo, valor=valor, saques=saques)
        elif opcao == 'e':
            extrato(saldo, depositos, saques)
        elif opcao == 'p':
            print("Saindo do processo...")
            break
        else:
            print("Erro: Operação inválida. Por favor, selecione novamente a operação desejada.")

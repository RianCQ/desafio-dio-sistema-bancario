menu = """
----- Menu -----
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [p] Parar

  => 
"""
saldo = 0
limite = 500
nSaques = 3
depositos = []
saques = []

def deposito(saldo: float, valor: float, depositos: list):
    if valor > 0.0:
        saldo = saldo + valor
        depositos.append(valor)
        print("Deposito realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")
    return saldo

def saque(saldo, valor: float, saques: list):
    if len(saques) < nSaques and valor <= limite :
        if saldo > valor :
            saldo = saldo - valor
            saques.append(valor)
            print("Saque realizado com sucesso.")
        else :
            print("Erro: Saldo insuficiente.")
    else :
        print("Erro: Saque negado.")
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

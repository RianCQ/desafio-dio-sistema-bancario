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



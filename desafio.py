menu = """
----- Menu -----
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [nc] Nova conta
  [nu] Novo usuário
  [lu] Lista usuários
  [p] Parar

  => """

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
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato) -> None:
    print("################ Extrato ##################")
    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")
    else :
        print(extrato)
        print()
        print(f"> Saldo total: R${saldo:.2f}")
    print("###########################################")

def filtrar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if cpf in usuario:
            return usuario
    return False

def criar_usuario(usuarios, cpf):
    nome = input("Informe o nome do usuário: ")
    data_nasc = input("Informe a data de nascimento (formato: dd-mm-aaaa): ")
    endereço = input("Endereço de usuário (logradouro, nº - bairro - cidade - sigla estado): ")
    usuarios.append({cpf: {"nome": nome, "data de nascimento": data_nasc, "endereço": endereço}})
    print("Usuário criado com sucesso.")

def criar_conta(agencia, usuario, contas):
    conta_nova = {"agencia": agencia, "numero_conta": len(contas)+1, "usuario": usuario}
    contas.append(conta_nova)
    print("Conta feita com sucesso.")

def lista_usuarios(usuarios):
    for user in usuarios:
        print(user)

def lista_contas(contas):
    for conta in contas:
        print(f"""
            ----------------------------------------
            Nº Conta: {conta['numero_conta']}
            Agência: {conta['agencia']}
            Titular: {conta['usuario']['nome']}
            ---------------------------------------
        """)
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "1000"

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
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 'nu':
            cpf = input("Informe o CPF (somente com números): ")
            if filtrar_usuario(usuarios, cpf):
                print("O CPF já está inscrito.")
            else:
                criar_usuario(usuarios, cpf)
        elif opcao == 'nc':
            cpf = input("Informe o CPF ligado a nova conta: ")
            if filtrar_usuario(usuarios, cpf):
                criar_conta(AGENCIA, cpf, contas)
            else:
                print("Usuário não detectado no sistema. Criação de conta não permitida.")
        elif opcao == 'lu':
            lista_usuarios(usuarios)
        elif opcao == 'lc':
            lista_contas(contas)
        elif opcao == 'p':
            print("Saindo do processo...")
            break
        else:
            print("Erro: Operação inválida. Por favor, selecione novamente a operação desejada.")

main()
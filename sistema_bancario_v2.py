def menu():
    menu = '''
    =============== MENU ===============
    [0] Depositar
    [1] Sacar
    [2] Extrato

    [3] Nova conta    
    [4] Novo Usuário
    [5] Listar contas

    [9] Sair
            
    =====================================
    '''
    return input(menu)

def depositar(extrato, saldo, valor_deposito):
    if valor_deposito >= 30:
        saldo += float(valor_deposito)        
        extrato += f'+ R$ {valor_deposito:.2f}\n'
        print(f'Depósito de R$ {valor_deposito} concluído com sucesso, seu saldo atual é R$ {saldo}')
    else:
        print('O valor mínimo para depósito é R$ 30')

    return saldo, extrato

def sacar(LIMITE_SAQUE, limite, saldo, extrato, valor_saque):
    if LIMITE_SAQUE <= 0:
        print('Limite de saques atingido')
    elif valor_saque >= limite:
        print('Seu limite diário foi atingido')
    elif valor_saque <= saldo:
        LIMITE_SAQUE = LIMITE_SAQUE - 1
        saldo -= valor_saque
        extrato += f'- R$ {valor_saque:.2f} \n'
        print(f'Retire seu dinheiro, saque realizado com sucesso seu saldo atual é R$ {saldo}')
    else:
        print('Saldo indisponível.')

    return saldo, extrato

def consultarExtrato(saldo, extrato):

    print(f'''
        =============== Extrato ===============

        {extrato if saldo > 0 else 'Não foram realizadas movimentações.'}

        Saldo total -> R$ {saldo}
        
        =======================================
    ''')

    return saldo, extrato

def criarUsuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf,"endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criarConta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, criação de conta encerrado")

def listarContas(contas):
    for conta in contas:
        linha = f'''
            Agência: {conta['agencia']}
            C/C: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
        '''
        print(linha)

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    limite = 500
    usuarios = []
    contas = []

    while True: 
        opcao = menu()

        if opcao == '0':
            valor_deposito = float(input("Qual valor deseja depositar?"))
            saldo, extrato = depositar(extrato, saldo, valor_deposito)
        elif opcao == '1':
            valor_saque = float(input('Qual valor desejar sacar?'))
            saldo, extrato = sacar(
                LIMITE_SAQUE = LIMITE_SAQUE, 
                limite = limite, 
                saldo = saldo, 
                extrato = extrato, 
                valor_saque = valor_saque,
                )
        elif opcao == '2':
            saldo, extrato = consultarExtrato(saldo, extrato)
        elif opcao == '3':
            numero_conta = len(contas) + 1
            conta = criarConta(agencia = AGENCIA, numero_conta = numero_conta, usuarios = usuarios)

            if conta:
                contas.append(conta)
        elif opcao == '4':
            criarUsuario(usuarios)
        elif opcao == '5':
            listarContas(contas)

        elif opcao == '9':
            break
        
        else:
            print("Opção inválida, selecione novamente")

main()

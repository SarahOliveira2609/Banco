import time #biblioteca usada para dar pausas no programa (time.sleep(tempo))
import getpass #biblioteca usada para ocultar a senha digitada no terminal

pessoa = [] #lista que guarda os dados dos clientes cadastrados no sistema

def cadastrar(): #coleta os dados de clintes novos
    nome = str(input("Digite o nome do cliente:"))
    idade = int(input("Digite a idade do cliente:"))
    cpf = input("Digite o cpf do cliente:")
    telefone = input("Digite o telefone do cliente:")
    email = str(input("Digite o email do cliente:"))
    senha = getpass.getpass("Digite a senha do cliente:")
    
    time.sleep(1)

    for user in pessoa: #verifica se já existe um cliente com o mesmo cpf cadastrado
        if cpf == user['cpf']:
            print("Já existe um cliente com esses dados cadastrados!")
            return #interromp a função caso encontre um cliente com o mesmo cpf
        
    novo_cliente = { #cria um dicionario com todos os dados do novo cliente
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
        'telefone': telefone,
        'email': email,
        'senha': senha,
        #saldo e historico começam vazios
        'saldo': 0,
        'historico': []}
    pessoa.append(novo_cliente) #add novo usuario na lista de clientes geral

    print("Cadastro realizado com sucesso!")
    print("Redirecionando para página de Login...")
    time.sleep(1)
    login() #redireciona para função de login

def login():
    tentar = 0 #contator de tentativas de login

    while True:
        cpf_login = input("Digite o cpf:")
        senha_login = getpass.getpass("Digite a senha:")

        encontrado = None #começa como None até achar o usuário correspondente ao cpf e senha digitados, caso contrário, permanece como None

        for user in pessoa: #percorre a lista de clientes para fazer a verficação
            if cpf_login == user['cpf'] and senha_login == user['senha']: #guarda o usuário encontrado 
                encontrado = user #para a busca caso encontre um usuário com o cpf e senha digitados
                break
        if encontrado:
            print("Login realizado com sucesso!")
            menu_principal(encontrado)#entra no menu principal do usuário encontrado    
            break
        else:
            tentar += 1 #incrementa o contador de tentativas caso não encontre um usuário com o cpf e senha digitados
            print("Nenhum usuário cadastrado com esses dados. Por favor, tente novamente.")
            if tentar == 3: #bloqueia o login após 3 tentativas falhas
                print("Você atingiu o número máximo de tentativas.")
                return          
        
def menu_principal(usuario):

    while True:
        escolha_menu = int(input("Escolha uma opção:\n" \
        "[1] Saldo\n[2] Depósito\n[3] Saque\n[4] Transferência\n [5] Histórico\n [6] Sair\n"))
        
        if escolha_menu == 1:
            print(f"Seu saldo é de R${usuario['saldo']:.2f}")
            usuario['historico'].append(f"Consulta de saldo: R${usuario['saldo']}")

        elif escolha_menu == 2:
            deposito = float(input("Digite o valor do despósito: R$"))
            usuario['saldo'] += deposito
            usuario['historico'].append(f"Depósito: R${deposito}")
            print(f"Seu depósito foi realizado com sucesso! Seu novo saldo é de R${usuario['saldo']:.2f}")

        elif escolha_menu == 3:
            saque = float(input("Digite o valor que deseja sacar: R$"))
            if saque > usuario['saldo']:
                print("Saldo insuficiente!")
            else:
                usuario['saldo'] -= saque
                usuario['historico'].append(f"Saque: R${saque}")
                print(f"Saque realizado com sucesso! Seu novo saldo é de R${usuario['saldo']:.2f}")
        
        elif escolha_menu == 4:
            nome_destino = str(input("Digite o nome do destinátario:"))
            valor_destino = float(input("Digite o valor da transferência: R$"))
            if valor_destino > usuario['saldo']:
                print("Saldo insuficiente!")
            else:
                usuario['saldo'] -= valor_destino
                usuario['historico'].append(f"Transferência para {nome_destino}: R${valor_destino}")
                print(f"Transferência realizada para {nome_destino} com o valor de {valor_destino}! Seu novo saldo é de R${usuario['saldo']:.2f}")
        
        elif escolha_menu == 5:
            if not usuario['historico']:
                print("Nenhuma transação realizada ainda.")
            else:
                for item in usuario['historico']:
                    print(item)

        else:
            print("Saindo do sistema...")
            time.sleep(1)
            break

   
while True:
    print("=-" * 20)
    print("Bem-Vindo ao OliverBank")
    print("=-" * 20)
    time.sleep(0.3)

    escolha = int(input("Escolha uma opção:\n" \
    "[1] Cadastrar Cliente\n" \
    "[2] Fazer Login\n" \
    "[3] Sair\n"))

    if escolha == 1:
        cadastrar()
    elif escolha == 2:
        login()
    else: 
        break   







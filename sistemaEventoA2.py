listaUsuarios = []
cadastros = []


def alterarNome():
    procurar = input("Insira o email do usuário que deseja alterar o nome: ")
    alterar = input("Insira o novo nome para alteração: ")
    for cadastro in listaUsuarios:
        if(procurar == cadastro["email"]):
            cadastro["nome"] = alterar
            print("Usuário alterado de {} para {}" .format(cadastro["email"], alterar))
    for cadastro in cadastros:
        separar = cadastro.split(" ")
        if(procurar == separar[3]):
            cadastros.remove(cadastro)
            usuarioAtualizado = separar
            usuarioAtualizado[1] = alterar
            usuarioAtualizado = usuarioAtualizado[0] + " " + usuarioAtualizado[1] + " " + usuarioAtualizado[2] + " " + usuarioAtualizado[3]
            cadastros.append(usuarioAtualizado)
    main()

def removerUsuario():
    remover = input("Digite o email do usuário que deseja remover: ")
    for cadastro in listaUsuarios:
        if(remover == cadastro["email"]):
            listaUsuarios.remove(cadastro)
            print("Usuário excluído!")
        else:
            print("O email não está na lista!")
            main()
    for cadastro in cadastros:
        separar = cadastro.split(" ")
        if(remover == separar[3]):
            cadastros.remove(cadastro)
    main()

def verificarNome():
    nome = input("Digite o nome que deseja procurar: ")
    for usuario in listaUsuarios:
        if(nome == usuario["nome"]):
            print("{0} possui cadastro!" .format(nome))
        else:
            print("{0} não possui cadastrado!" .format(nome))
    main()
    
def listarAlfabetica():
    print("Lista por ordem alfabética: ")
    listaAlfabetica = sorted(cadastros)
    for nome in listaAlfabetica:
        print("{0}".format(nome))
    main()
    
def listarCadastro(listaUsuarios):
    print("Lista por ordem de cadastro: ")
    num = 1
    for cadastro in listaUsuarios:
        print("{0} - Nome: {1}, Email: {2}".format(num, cadastro["nome"], cadastro["email"]))
        num = num + 1
    print(cadastros)
    print(listaUsuarios)
    main()

def cadastrarUsuario():
    usuarios = {}
    usuarios["nome"] = input("Digite o nome completo do usuário: ")
    usuarios["email"] = input("Digite o email do usuário: ")
    cadastros.append("Nome: {0} Email: {1}".format(usuarios["nome"], usuarios["email"]))
    return usuarios
        

def mostrarMenu():
    print("----------------------------------Menu----------------------------------")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários por ordem de cadastro")
    print("3 - Listar usuários por ordem alfabética")
    print("4 - Verificar se um usuário faz parte da lista através do nome")
    print("5 - Remover usuário")
    print("6 - Alterar nome de usuário")
    print("7 - Fechar programa")
        
def main():
    mostrarMenu()

    option = int(input("Escolha uma opção: "))
    while(option < 1 or option > 7):
        print("Você escolheu uma opção inválida! Tente novamente.")
        option = int(input("Escolha uma opção: "))

    if(option == 1):
        usuarios = cadastrarUsuario()
        listaUsuarios.append(usuarios)
        main()
    elif(option == 2):
       listarCadastro(listaUsuarios)
    elif(option == 3):
        listarAlfabetica()
    elif(option == 4):
        verificarNome()
    elif(option == 5):
        removerUsuario()
    elif(option == 6):
        alterarNome()
    else:
        breakpoint

if __name__ == "__main__":
    main()

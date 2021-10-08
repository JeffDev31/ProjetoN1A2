def exibirMenu():
    print("==== Digite 1 para cadastrar novo usuário: ====\n")
    print("==== Digite 2 para exibir todos os usuários por ordem de cadastro: ====\n")
    print("==== Digite 3 para exibir todos os usuários por ordem alfabética: ====\n")
    print("==== Digite 4 para verficar o dado de um usuário pelo seu nome: ====\n")
    print("==== Digite 5 para verficar o dado de um usuário pelo seu e-mail: ====\n")
    print("==== Digite 6 para remover um usuário cadastrado: ====\n")
    print("==== Digite 7 para alterar o nome de um usuário buscando-o por seu e-mail: ====\n")
    pass

def escolhaMenu():
    escolha = input()
    if (escolha == 1):
        nomeNovoUsuario = input("dgite o nome completo do novo Usuário:\n")
     #   dicionarioUsuarios.append(nomeNovoUsuario)
        emailNovoUsuario = input("Digite o e-mail do novo Usuário:\n")
    elif (escolha == 2):
        print("batata")


def main():
    listaDicionarioUsuarios = []
    dicionarioUsuarios = {}     
    exibirMenu()
    escolhaMenu()   
    pass



if __name__ == "__main__":
    main()
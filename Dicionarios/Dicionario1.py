def perguntar():
    resposta = input("\n ----- O que deseja realizar? ----- \n" +
            "| <I> - Para Inserir um usuário. \n" +
            "| <P> - Para pesquisar um usuário. \n" +
            "| <E> - Para excluir um usuário. \n" +
            "| <L> - Para listar um usuário. \n" +
            "| <S> - Para Sair. \n" +
            " > ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("\nDigite o nome: ").upper(),
                         input("Digite a última data de acesso: ").upper(),
                         input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
        lista = dicionario.get(chave)
        if lista!=None:
            print("\nNome...........: " + lista[0])
            print("Último acesso..: " + lista[1])
            print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("\nObjeto excluído com sucesso! ")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("\nObjeto......")
        print("Login: ", chave)
        print("Dados: ", valor)

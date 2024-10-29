import os

# Dicionario pra guardar os restaurantes
restaurantes = [{'nome':'Pizzaria Sucesso','categoria':'Italiana','ativo':False},
                {'nome':'Querido Donuts','categoria':'Doceria','ativo':True},
                {'nome':'Sushi e Cia','categoria':'Japonesa','ativo':False}]

def exibir_nome_prog():
    print('______Sabor Express______\n')

# Menu da app
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Bye bye')

def voltar_menu():
    input('\nDigite uma tecla para retornar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida')
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha) 
    print()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    inputs: nome do restaurante e categoria
    outputs: add o restaurante a lista de restaurantes 
    ''' #docstring serve para explicar o que será feito dentro daquela função
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def alternar_estado_restaurante():
    '''Essa função é responsável por alternar o estado de ativação do restaurante'''
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante=input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado=False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo'] #not é um operador que troca o valor do valor que a variavel tem
            mensagem = (f'O restaurante{nome_restaurante} foi ativado com sucesso') if restaurante['ativo'] else (f'O restaurante {nome_restaurante}foi desativado com sucesso')
            print(mensagem)
        if not restaurante_encontrado:
            print('O restaurante não foi encontrado')    
    voltar_menu()
def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados'''
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)}|{'Categoria'.ljust(20)}| {'Status'}')
    for restaurante in restaurantes:  
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'  #ternário(condicao toda em uma linha, 1ºvdd e segundo falso)
        print(f'- {nome_restaurante.ljust(20)} |{categoria.ljust(20)} | {ativo}')
    voltar_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Selecione uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:  
        opcao_invalida()

def main():
    os.system('clear')  
    exibir_nome_prog() 
    exibir_opcoes()  
    escolher_opcao()

# Para fazer com que esse programa seja o programa principal da app
if __name__ == '__main__':
    main()
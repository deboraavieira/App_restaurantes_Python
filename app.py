import os
from restaurantes import *

# Dicionario pra guardar os restaurantes ( IMPORTAR ARQUIVO CSV)
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

#metodo para cadastrar restaurante
def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    inputs: nome do restaurante e categoria
    outputs: add o restaurante a lista de restaurantes 
    ''' 
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    localizacao = input(f'Digite a localização do restaurante {nome_restaurante}: ')
    status = input(f'Digite o status do restaurante {nome_restaurante}: ') 
    tipo_servico = input(f'Digite o tipo de serviço que o restaurante {nome_restaurante} fornece: ') 
    dados_restaurante = {'nome':nome_restaurante,'categoria':categoria,'localizacao':localizacao,'status':status,'tipo_servico':tipo_servico}
    restaurantes.append(dados_restaurante)  # inseria no dicionario de restaurantes
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()
 
 #metodo para listar restaurante:   
def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados'''
    exibir_subtitulo('Listando os restaurantes')
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    else:
        print(f"{'Nome do restaurante'.ljust(22)}|{'Categoria'.ljust(20)}| {'Localização'.ljust(20)}| {'Status'.ljust(20)}| {'Tipo de Serviço'}")
        for restaurante in restaurantes:  
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            localizacao = restaurante['localizacao']
            status = restaurante['status']
            tipo_servico = restaurante['tipo_servico']
            print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {localizacao.ljust(20)} | {status.ljust(20)} | {tipo_servico}")
    voltar_menu()

    #metodo alterar restaurante:
def alterar_restaurante():
    '''Essa função é responsável por alterar os dados de um restaurante'''
    exibir_subtitulo('Alterar dados do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            categoria = input(f'Digite a nova categoria do restaurante {nome_restaurante} (deixe em branco para manter): ')
            localizacao = input(f'Digite a nova localização do restaurante {nome_restaurante} (deixe em branco para manter): ')
            status = input(f'Digite o novo status do restaurante {nome_restaurante} (deixe em branco para manter): ')
            tipo_servico = input(f'Digite o novo tipo de serviço do restaurante {nome_restaurante} (deixe em branco para manter): ')
            if categoria:
                restaurante['categoria'] = categoria
            if localizacao:
                restaurante['localizacao'] = localizacao
            if status:
                restaurante['status'] = status
            if tipo_servico:
                restaurante['tipo_servico'] = tipo_servico
            print(f'Os dados do restaurante {nome_restaurante} foram atualizados com sucesso!')
            break
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')    
    voltar_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Selecione uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_restaurante()
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
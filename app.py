import pandas as pd
import os
from restaurantes import *
from restEspecialidade import *
restaurantes = pd.read_csv('/Users/deboravieira/Documents/GitHub/projPython/ListaRestaurantes.csv')
restaurantes.head(5)
print(restaurantes)
#nome da app
def exibir_nome_prog():
    print('______Sabor À Mão______\n')
# Menu da app
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar dados do restaurante')
    print('4. Eliminar restaurante')
    print('5. Escolher categoria')
    print('6. Sair\n')
#função para finalizar a app
def finalizar_app():
    exibir_subtitulo('Bye bye')
#função de retorno ao menu principal
def voltar_menu():
    input('\nDigite uma tecla para retornar ao menu principal')
    main()
#função pra mostrar a opção inválida
def opcao_invalida():
    print('Opção inválida')
    voltar_menu()
#função para subtitulo
def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha) 
    print()
# função para inserir um restaurante ao arquivo
def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome= input('Digite o nome do restaurante que deseja cadastrar: ')
    Categoria = input(f'Digite o nome da categoria do restaurante {nome}: ')
    Localizacao = input(f'Digite a localização do restaurante {nome}: ')
    status = input(f'Digite o status do restaurante {nome}: ') 
    pagamento = ('cartão')    
    # Serve para criar uma nova linha no DataFrame
    novo_restaurante = pd.DataFrame({
        'Nome': [nome],
        'Categoria': [Categoria],
        'Localização': [Localizacao],
        'Status': [status],
        'Pagamento': [pagamento]
    })
    # Concatena com o existente
    global restaurantes
    restaurantes = pd.concat([restaurantes, novo_restaurante], ignore_index=True)
    # Salva em CSV
    restaurantes.to_csv('/Users/deboravieira/Documents/GitHub/projPython/ListaRestaurantes.csv', index=False)
    print(f'O restaurante {nome} foi cadastrado com sucesso!')
    voltar_menu()

 #metodo para listar restaurante cadastrados   
def listar_restaurantes():
     exibir_subtitulo('Listando os restaurantes')
     print(restaurantes)  
    
     voltar_menu()
     
# Função para alterar um restaurante existente
def alterar_restaurante():
    exibir_subtitulo('Alterar dados do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar: ')
    if nome_restaurante in restaurantes['Nome'].values: 
        Categoria = input(f'Digite a nova categoria do restaurante {nome_restaurante} : ')
        localizacao = input(f'Digite a nova localização do restaurante {nome_restaurante} : ')
        status = input(f'Digite o novo status do restaurante {nome_restaurante} : ')
        tipo_servico = input(f'Digite o novo tipo de serviço do restaurante {nome_restaurante} : ')
        # Faz o update nos valores
        idx = restaurantes.index[restaurantes['Nome'] == nome_restaurante].tolist()[0] 
        if Categoria:
            restaurantes.at[idx, 'Categoria'] = Categoria  
        if localizacao:
            restaurantes.at[idx, 'Localização'] = localizacao
        if status:
            restaurantes.at[idx, 'Status'] = status  
        if tipo_servico:
            restaurantes.at[idx, 'Pagamento'] = tipo_servico  
        # Salva as alterações em CSV
        restaurantes.to_csv('/Users/deboravieira/Documents/GitHub/projPython/ListaRestaurantes.csv', index=False)
        print(f'Os dados do restaurante {nome_restaurante} foram atualizados com sucesso!')
    else:
        print('O restaurante não foi encontrado.')    
    voltar_menu()
    
#função para eliminar restaurante    
def eliminar_restaurante():
    exibir_subtitulo('Eliminar Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja eliminar: ')
    # Verifica se o restaurante existe
    if nome_restaurante in restaurantes['Nome'].values:
        # Remove o restaurante
        restaurantes.drop(restaurantes[restaurantes['Nome'] == nome_restaurante].index, inplace=True)
        # Salva as alterações em CSV
        restaurantes.to_csv('/Users/deboravieira/Documents/GitHub/projPython/ListaRestaurantes.csv', index=False)
        print(f'O restaurante {nome_restaurante} foi eliminado com sucesso!')
    else:
        print('O restaurante não foi encontrado.')    
    voltar_menu()    

#função para escolher o restaurante pela categoria:
def escolher_categoria():
    exibir_subtitulo('Escolher Restaurante por Categoria')
    print('\nCategorias disponíveis:')
    print('1. Hamburgueria')
    print('2. Italiano')
    print('3. Asiático')
    print('4. Pastelaria')
    print('5. Saudável')
    print('6. Luso-Brasileiro')
    try:
        opcao = int(input('\nEscolha uma categoria (1-6): '))
        if opcao == 1:  
            # Hamburgueria
            nome_rest = input('Digite o nome da hamburgueria: ')
            localizacao = input('Digite a localização: ')
            status = input('Digite o status (Aberto/Fechado): ')
            # Lista de molhos disponíveis
            print('\nMolhos disponíveis: cheddar, verde, barbecue, mostarda, caeser, kebab, maionese, ketchup, coctail, picante')
            tmolho = input('Escolha o tipo de molho: ')
            # Criar instância de Hamburgueria
            hamburgueria = Hamburgueria(nome_rest, localizacao, status, tmolho)
            hamburgueria.mostra_restaurante()
            hamburgueria.escolheMolho(tmolho)
        elif opcao == 2:  
            # Italiano
            nome_rest = input('Digite o nome do restaurante Italiano desejado: ')
            localizacao = input('Digite a localização: ')
            status = input('Digite o status (Aberto/Fechado): ')
            #Lista de italiano
            print('\nTipo de cardápio: Massa, Pizza')
            tmenu = input('Escolha o tipo de menu: ') 
            # Criar instância de Italiano 
            italiano = Italiano(nome_rest, localizacao, status, tmenu) 
            italiano.mostra_restaurante()
            italiano.mostraCardapio()
        elif opcao == 3:  
            # Asiático
            nome_rest = input('Digite o nome do restaurante asiático: ')
            localizacao = input('Digite a localização: ')
            status = input('Digite o status (Aberto/Fechado): ')
            #Lista de rodízios disponíveis
            print('\nRodízios disponíveis: simples, premium, tradicional, supreme')
            trodizio = input('Escolha o tipo de rodízio: ')
           # Criar instância de Asiático
            asiatico = Asiatico(nome_rest, localizacao, status, trodizio)
            asiatico.mostra_restaurante()
            asiatico.escolheRodizio(trodizio)
        elif opcao == 4:  
            # Pastelaria
            nome_rest = input('Digite o nome da pastelaria: ')
            localizacao = input('Digite a localização: ')
            status = input('Digite o status (Aberto/Fechado): ')
            
            #Lista de doces disponíveis
            print('\nDoces disponíveis: bolos, pastel de nata, docinho, miniaturas, eclair, bolachas, tartes, quindim')
            tdoce = input('Escolha o tipo de doce: ')
            
            #Criar instância de Pastelaria
            pastelaria = Pastelaria(nome_rest, localizacao, status, tdoce)
            pastelaria.mostra_restaurante()
            pastelaria.escolheDoce(tdoce)
        elif opcao == 5: 
            # Saudável
            nome_rest = input('Digite o nome do restaurante saudável: ')
            localizacao = input('Digite a localização: ')
            status = input('Digite o status (Aberto/Fechado): ')
            #Lista de smothies disponíveis
            print('\nSmothies disponíveis: verde, imunidade, energizante, antioxidante, detox, refrescante')
            tsmothie = input('Escolha o tipo de smoothie: ')
            #Criar instância de Saudável
            saudavel = Saudavel(nome_rest, localizacao, status, tsmothie)
            saudavel.mostra_restaurante()
            saudavel.mostraSmothie(tsmothie)
        elif opcao == 6:  
            # Luso-Brasileiro
            nome_rest = input('Digite o nome do restaurante luso-brasileiro: ')
            localizacao = input('Digite a localização: ')
            status = input('Digite o status (Aberto/Fechado): ')
            #Lista de luso-brasileiro
            print('\nTipo de culinária: portuguesa, brasileira')
            tculinaria = input('Escolha o tipo de culinária: ')
            #Criar instância Luso-brasileiro
            luso_brasileiro = LusoBrasileiro(nome_rest, localizacao, status, tculinaria)
            luso_brasileiro.mostra_restaurante()
            luso_brasileiro.mostraCulinaria()
        else:
            print('Opção inválida!')
    except ValueError:
        print('Por favor, digite um número válido!')
    
    voltar_menu()
#função para as opções escolhidas    
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
            eliminar_restaurante()
        elif opcao_escolhida == 5:
            escolher_categoria()
        elif opcao_escolhida == 6:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:  
        opcao_invalida()
#função main
def main():
    os.system('clear')  
    exibir_nome_prog() 
    exibir_opcoes()  
    escolher_opcao()

# Para fazer com que esse programa seja o programa principal da app
if __name__ == '__main__':
    main()
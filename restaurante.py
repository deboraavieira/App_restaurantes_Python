#criação da classe restaurante
class Restaurante:
    contadorRestaurante = 0             #contador de restaurantes
    def __init__(self, nome,localizacao,status):
        self.pagamento = 'Cartão'      #atributo fixo, não passado como argumento
        self.nome = nome
        self.localizacao = localizacao  #bairros de lisboa
        self.status = status            #aberto/fechado
        Restaurante.contadorRestaurante += 1
        
    #definição dos método para mostrar as características do restaurante   
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Pagamento: {self.pagamento}
              ''')
        
    #função para mostrar o contador
    def mostra_contador():
        print(f'Número de restaurantes: {Restaurante.contadorRestaurante}')
    
    #função para mostrar o modo de pagamento
    def mostra_pagamento(self,pagamento):
        self.pagamento = pagamento
        print(f'O pagamento escolhido foi {self.pagamento}')
#criação da classe restaurantes
class Restaurante:
    def __init__(self, nome,localizacao,status,tservico):
        self.pagamento = 'Cartão'      #atributo fixo, não passado como argumento
        self.nome = nome
        self.localizacao = localizacao  #bairros de lisboa
        self.status = status            #aberto/fechado
        self.tservico = tservico         #delivery,takeaway,comer no local
    
    #definição dos métodos    
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Pagamento: {self.pagamento}
              ''')
    
        
    
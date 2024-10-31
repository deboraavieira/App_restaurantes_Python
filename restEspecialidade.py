from restaurantes import *

class Hamburgueria(Restaurante):
    def __init__(self, nome, localizacao, status, tservico,tmolho):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.molho = tmolho #cheddar,verde,barbecue,mostarda,caeser,kebab,maionese,ketchup, coctail,picante

     #definição de metodo
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Molho: {self.molho}
              Pagamento: {self.pagamento}
              ''')
    
class Italiano(Restaurante):
    def __init__(self, nome, localizacao, status, tservico, tmassa):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.massa = tmassa #espagetti,talharim,gnocchi,ravioli,tortelini,fusilli,penne,lasanha,fetuccini
    
    #definição de metodo
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Massa: {self.massa}
              Pagamento: {self.pagamento}
              ''')        
            
class Asiatico(Restaurante):
    def __init__(self, nome, localizacao, status, tservico, trodizio):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.trodizio = trodizio #sushi, sashimi,spring roll,pratos chineses,curry tailandês,noodles,temaki
        
     #definição de metodo
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Rodízio: {self.rodizio}
              Pagamento: {self.pagamento}
              ''')     

class Pastelaria(Restaurante):
    def __init__(self, nome, localizacao, status, tservico, tdoce):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.tdoce = tdoce  #bolo,pastel de nata, docinho, miniaturas,eclair,bolachas,tartes,quindim
        
     #definição de metodo
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Doçaria: {self.tdoce}
              Pagamento: {self.pagamento}
              ''')       
 
class Saudavel(Restaurante):
    def __init__(self, nome, localizacao, status, tservico, tsumo):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.tsumo = tsumo  #sumo verde, sumo da imunidade, sumo energizante, sumo antioxidante, sumo detox, sumo refrescante
        
     #definição de metodo
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Tipo de Sumo: {self.tsumo}
              Pagamento: {self.pagamento}
              ''')         
from restaurantes import *

class Hamburgueria(Restaurante):
    def __init__(self, nome, localizacao, status, tservico,tmolho):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.tmolho = tmolho #cheddar,verde,barbecue,mostarda,caeser,kebab,maionese,ketchup, coctail,picante

     #definição de metodo
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Molho: {self.tmolho}
              Pagamento: {self.pagamento}
              ''')
     
     
     #metodo para escolher molho   
    def escolheMolho(self,tmolho):
        print(f'O molho escolhido foi {tmolho}')

   
###################################################################################################################################################
    
class Italiano(Restaurante):
    def __init__(self, nome, localizacao, status, tservico, tmassa,tpizza):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.tmassa = tmassa #espagetti,talharim,gnocchi,ravioli,tortelini,fusilli,penne,lasanha,fetuccini
        self.tpizza = tpizza #quatro queijos,calabresa,frango com catupiry, peperoni, romana, havaiana, portuguesa
    
    #definição de metodo (herdado classe mãe - sobreposto)
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Massa: {self.massa}
              Pizza: {self.pizza}
              Pagamento: {self.pagamento}
              ''')   
    
    #metodo para escolher massa
    def escolheMassa(self,tmassa):
        print(f'A massa escolhida foi {tmassa}')

            
    #metodo para escolher pizza
    def escolhePizza(self,tpizza):
        print(f'A pizza escolhida foi {tpizza}')
    
     
        
 ###################################################################################################################################################           
class Asiatico(Restaurante):
    def __init__(self, nome, localizacao, status, tservico, trodizio):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.trodizio = trodizio #simples,premium,tradicional,supreme
        
     #definição de metodo (herdado classe mãe - sobreposto)
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Rodízio: {self.rodizio}
              Pagamento: {self.pagamento}
              ''')     
        
     #metodo para escolher o tipo de rodízio
    def escolheRodizio(self,trodizio):
        print(f'O rodízio escolhido foi {trodizio}')


###################################################################################################################################################
class Pastelaria(Restaurante):
    def __init__(self, nome, localizacao, status, tservico, tdoce):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.tdoce = tdoce  #bolos,pastel de nata, docinho, miniaturas,eclair,bolachas,tartes,quindim
        
     #definição de metodo (herdado classe mãe - sobreposto)
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Doçaria: {self.tdoce}
              Pagamento: {self.pagamento}
              ''')     
          
     #metodo para escolher o doce
    def escolheDoce(self,tdoce):
        print(f'O doce escolhido foi {tdoce}')
        
################################################################################################################################################### 
class Saudavel(Restaurante):
    def __init__(self, nome, localizacao, status, tservico, tsmothie):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.tsmothie = tsmothie  #smothie verde, smothie da imunidade, smothie energizante, smothie antioxidante, smothie detox, smothie refrescante
        
     #definição de metodo (herdado classe mãe - sobreposto)
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Tipo de Sumo: {self.tsumo}
              Pagamento: {self.pagamento}
              ''')  
     
     #metodo para mostrar o smothie
    def mostraSmothie(self,tsmothie):
        print(f'O smothie escolhido foi {tsmothie}')

###################################################################################################################################################
class LusoBrasileiro(Restaurante):
    def __init__(self, nome, localizacao, status, tservico, tculinaria,opcoes):
        super().__init__(nome, localizacao, status, tservico) #chama o construtor da classe mãe
        self.tculinaria = tculinaria  #portuguesa,brasileira
        self.opcoes = opcoes  #menu do dia, sugestão do chef, a la carte
        
     #definição de metodo (herdado classe mãe - sobreposto)
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Serviço: {self.tservico}
              Tipo de Culinária: {self.tculinaria}
              Opções de Menu: {self.opcoes}
              Pagamento: {self.pagamento}
              ''')     
    
     #metodo para mostrar o tipo de culinaria e escolher tipo de comida
    def mostraCulinaria(self):
        if self.tculinaria == 'brasileira':
            opcao_escolhida = (input('''Selecione uma opção: mineira, churrasco, nordestina, capixaba'''))
            if opcao_escolhida == 'mineira':
                print(f'Você escolheu um restaurante de culinária  brasileira com o tipo de comida {opcao_escolhida}')
            elif opcao_escolhida == 'churrasco':
                print(f'Você escolheu um restaurante de culinária  brasileira com o tipo de comida {opcao_escolhida}')
            elif opcao_escolhida == 'nordestina':
                print(f'Você escolheu um restaurante de culinária  brasileira com o tipo de comida {opcao_escolhida}')
            elif opcao_escolhida == 'capixaba':
                print(f'Você escolheu um restaurante de culinária  brasileira com o tipo de comida {opcao_escolhida}')
            else:
                print(f'Infelizmente não dispomos desse tipo de comida ainda.Tente novamente!')
        elif self.tculinaria == 'portuguesa':
            opcao_escolhida = (input('''Selecione uma opção: alentejana, transmontana, minhota, ribatejo'''))
            if opcao_escolhida == 'alentejana':
                print(f'Você escolheu um restaurante de culinária  portuguesa com tipo de comida {opcao_escolhida}')
            elif opcao_escolhida == 'transmontana':
               print(f'Você escolheu um restaurante de culinária  portuguesa com tipo de comida {opcao_escolhida}')
            elif opcao_escolhida == 'minhota':
              print(f'Você escolheu um restaurante de culinária  portuguesa com tipo de comida {opcao_escolhida}')
            elif opcao_escolhida == 'ribatejo':
                print(f'Você escolheu um restaurante de culinária  portuguesa com tipo de comida {opcao_escolhida}')
            else:
                print(f'Infelizmente não dispomos desse tipo de comida ainda.Tente novamente!')  
        else:
            print(f'Infelizmente não dispomos dessa culinária.Tente novamente!')        
     
            
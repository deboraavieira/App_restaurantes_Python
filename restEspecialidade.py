from restaurante import *
#definição das classes filhas
class Hamburgueria(Restaurante):
    def __init__(self, nome, localizacao, status,tmolho):
        super().__init__(nome, localizacao, status) #chama o construtor da classe mãe
        self.tmolho = tmolho #cheddar,verde,barbecue,mostarda,caeser,kebab,maionese,ketchup, coctail,picante

     #definição de metodo
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Molho: {self.tmolho}
              Pagamento: {self.pagamento}
              ''')
     
     #metodo para escolher molho   
    def escolheMolho(self,tmolho):
        print(f'O molho escolhido foi {tmolho}')
###################################################################################################################################################
class Italiano(Restaurante):
    def __init__(self, nome, localizacao, status,tmenu):
        super().__init__(nome, localizacao, status) #chama o construtor da classe mãe
        self.tmenu = tmenu
    
    #definição de metodo (herdado classe mãe - sobreposto)
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Cardápio: {self.tmenu}
              Pagamento: {self.pagamento}
              ''')   
    
     #metodo para mostrar o escolher tipo de comida
    def mostraCardapio(self):
        if self.tmenu == 'Massa':
            opcao_selecionada = (input('Selecione uma opção: espagetti,talharim,gnocchi,ravioli,tortelini,fusilli,penne,lasanha,fetuccini: '))
            if opcao_selecionada == 'espagetti':
                print(f'Você escolheu um restaurante de culinária  italiana com a massa {opcao_selecionada}')
            elif opcao_selecionada == 'talharim':
                print(f'Você escolheu um restaurante de culinária  italiana com a massa {opcao_selecionada}')
            elif opcao_selecionada == 'gnocchi':
                print(f'Você escolheu um restaurante de culinária  italiana com a massa {opcao_selecionada}')
            elif opcao_selecionada == 'ravioli':
                print(f'Você escolheu um restaurante de culinária  italiana com a massa {opcao_selecionada}')
            elif opcao_selecionada == 'tortelini':
                print(f'Você escolheu um restaurante de culinária  italiana com a massa {opcao_selecionada}')
            elif opcao_selecionada == 'fusilli':
                print(f'Você escolheu um restaurante de culinária  italiana com a massa {opcao_selecionada}')   
            elif opcao_selecionada == 'penne':
                print(f'Você escolheu um restaurante de culinária  italiana com a massa {opcao_selecionada}') 
            elif opcao_selecionada == 'lasanha':
                print(f'Você escolheu um restaurante de culinária  italiana com a massa {opcao_selecionada}') 
            elif opcao_selecionada == 'fetuccini':
                print(f'Você escolheu um restaurante de culinária  italiana com a massa {opcao_selecionada}')      
            else:
                print(f'Infelizmente não dispomos desse tipo de massa ainda.Tente novamente!')
        elif self.tmenu == 'Pizza':
            opcao_selecionada = (input('Selecione uma opção: quatro queijos,calabresa,frango com catupiry, peperoni, romana, havaiana, portuguesa: '))
            if opcao_selecionada == 'quatro queijos':
                print(f'Você escolheu um restaurante de culinária  italiana com a pizza {opcao_selecionada}')
            elif opcao_selecionada == 'calabresa':
                print(f'Você escolheu um restaurante de culinária  italiana com a pizza {opcao_selecionada}')
            elif opcao_selecionada == 'frango com catupiry':
                print(f'Você escolheu um restaurante de culinária  italiana com a pizza {opcao_selecionada}')
            elif opcao_selecionada == 'peperoni':
                print(f'Você escolheu um restaurante de culinária  italiana com a pizza {opcao_selecionada}')
            elif opcao_selecionada == 'romana':
                print(f'Você escolheu um restaurante de culinária  italiana com a pizza {opcao_selecionada}')
            elif opcao_selecionada == 'havaiana':
                print(f'Você escolheu um restaurante de culinária  italiana com a pizza {opcao_selecionada}')   
            elif opcao_selecionada == 'portuguesa':
                print(f'Você escolheu um restaurante de culinária  italiana com a pizza {opcao_selecionada}')    
            else:
                print(f'Infelizmente não dispomos desse tipo de pizza ainda.Tente novamente!')     
        else:
            print(f'Infelizmente não dispomos desse menu.Tente novamente!')        
 ###################################################################################################################################################           
class Asiatico(Restaurante):
    def __init__(self, nome, localizacao, status,trodizio):
        super().__init__(nome, localizacao, status) #chama o construtor da classe mãe
        self.trodizio = trodizio #simples,premium,tradicional,supreme
        
     #definição de metodo (herdado classe mãe - sobreposto)
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Rodízio: {self.trodizio}
              Pagamento: {self.pagamento}
              ''')     
        
     #metodo para escolher o tipo de rodízio
    def escolheRodizio(self,trodizio):
        print(f'O rodízio escolhido foi {trodizio}')

###################################################################################################################################################
class Pastelaria(Restaurante):
    def __init__(self, nome, localizacao, status,tdoce):
        super().__init__(nome, localizacao, status) #chama o construtor da classe mãe
        self.tdoce = tdoce  #bolos,pastel de nata, docinho, miniaturas,eclair,bolachas,tartes,quindim
        
     #definição de metodo (herdado classe mãe - sobreposto)
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Doçaria: {self.tdoce}
              Pagamento: {self.pagamento}
              ''')     
          
     #metodo para escolher o doce
    def escolheDoce(self,tdoce):
        print(f'O doce escolhido foi {tdoce}')
        
################################################################################################################################################### 
class Saudavel(Restaurante):
    def __init__(self, nome, localizacao, status,tsmothie):
        super().__init__(nome, localizacao, status) #chama o construtor da classe mãe
        self.tsmothie = tsmothie  #smothie verde, smothie da imunidade, smothie energizante, smothie antioxidante, smothie detox, smothie refrescante
        
     #definição de metodo (herdado classe mãe - sobreposto)
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Smothie: {self.tsmothie}
              Pagamento: {self.pagamento}
              ''')  
     
     #metodo para mostrar o smothie
    def mostraSmothie(self,tsmothie):
        print(f'O smothie escolhido foi {tsmothie}')

###################################################################################################################################################
class LusoBrasileiro(Restaurante):
    def __init__(self, nome, localizacao, status, tculinaria):
        super().__init__(nome, localizacao, status) #chama o construtor da classe mãe
        self.tculinaria = tculinaria  #portuguesa,brasileira
        
     #definição de metodo (herdado classe mãe - sobreposto)
    def mostra_restaurante(self):
        print(f''' Características do restaurante:
              Nome: {self.nome}
              Localização: {self.localizacao}
              Status: {self.status}
              Tipo de Culinária: {self.tculinaria}
              Pagamento: {self.pagamento}
              ''')     
    
     #metodo para mostrar o tipo de culinaria e escolher tipo de comida
    def mostraCulinaria(self):
        if self.tculinaria == 'brasileira':
            opcao_escolhida = (input('Selecione uma opção: mineira, churrasco, nordestina, capixaba: '))
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
            opcao_escolhida = (input('Selecione uma opção: alentejana, transmontana, minhota, ribatejo: '))
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
     
            
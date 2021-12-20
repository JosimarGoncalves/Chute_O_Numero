#Projeto Chute o numero

import random

class ChuteONumero:
    def _init_(self):
        self.valorAleatorio = 0
        self.valorMinimo = 1
        self.valorMaximo = 100
        self.tentarNovamente = True
        
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentarNovamente == True:
                if int(self.valorDoChute) > self.valorAleatorio:
                    print('Chute um numero mais baixo!')
                    self.PedirValorAleatorio()
                elif int(self.valorDoChute) < self.valorAleatorio:
                    print('Chute um numero mais alto!')
                    self.PedirValorAleatorio()
                if int(self.valorDoChute) == self.valorAleatorio:
                    self.tentarNovamente = False
                    print('Acertou o numero')
        except:
            print('Favor digitar numero apenas')
            self.Iniciar()
          
                
           


    def PedirValorAleatorio(self):
        self.valorDoChute = input('Chute um nuemro de: 0 a 100')


    def GerarNumeroAleatorio(self):
        self.valorAleatorio = random.randint(1,100)

chute = ChuteONumero()
chute.Iniciar()
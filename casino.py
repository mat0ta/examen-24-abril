import threading
import multiprocessing
import time
import random
import names

class Casino():
    def __init__(self):
        self.casa = 50000
        self.ruleta = [1, 36]
        self.crupier_wait_time = 3000 # 3 segundos
        self.numero = 0
    
    def apostar_a_numero(self, jugador, apuesta):
        jugador.saldo -= apuesta
        self.casa += apuesta
        if self.numero == jugador.numero:
            jugador.saldo += apuesta * 36
            self.casa -= apuesta * 36
            print('El jugador {} ha ganado  ' + str(apuesta * 36) + '  euros'.format(jugador.nombre))
        else:
            print('El jugador {} ha perdido ' + str(apuesta) + ' euros'.format(jugador.nombre))
        
    def apostar_a_paridad(self, jugador):
        jugador.saldo -= 10
        self.casa += 10
        if self.numero % 2 == jugador.paridad:
            jugador.saldo += 20
            self.casa -= 20
            print('El jugador {} ha ganado 20 euros'.format(jugador.nombre))
        else:
            print('El jugador {} ha perdido 10 euros'.format(jugador.nombre))

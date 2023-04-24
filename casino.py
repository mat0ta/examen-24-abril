import threading
import multiprocessing
import time
import random
import names

class Jugador():
    def __init__(self):
        self.nombre = ''
        self.numero = 0
        self.paridad = 0
        self.saldo = 0
        self.martin_gala = 0
class Casino():
    def __init__(self):
        self.casa = 50000
        self.ruleta = [1, 36]
        self.crupier_wait_time = 3000 # 3 segundos
        self.numero = 0
    
    def apostar_a_numero(self, jugador, apuesta):
        if jugador.martin_gala > 0:
            apuesta = apuesta * jugador.martin_gala
        jugador.saldo -= apuesta
        self.casa += apuesta
        if self.casa >= apuesta * 35:
            if self.numero == jugador.numero:
                jugador.saldo += apuesta * 36
                self.casa -= apuesta * 36
                print(f'El jugador {jugador.nombre} ha ganado  ' + str(apuesta * 36) + '  euros')
            else:
                print(f'El jugador {jugador.nombre} ha perdido ' + str(apuesta) + ' euros')
        else:
            print('La banca no tiene suficiente dinero para pagar la apuesta')
        
    def apostar_a_paridad(self, jugador):
        jugador.saldo -= 10
        self.casa += 10
        if self.casa >= 10:
            if self.numero % 2 == jugador.paridad:
                jugador.saldo += 20
                self.casa -= 20
                print(f'El jugador {jugador.nombre} ha ganado 20 euros')
            else:
                print(f'El jugador {jugador.nombre} ha perdido 10 euros')
        else:
            print('La banca no tiene suficiente dinero para pagar la apuesta')

    def crupier(self):
        while True:
            time.sleep(self.crupier_wait_time)
            self.numero = random.randint(0, 36)
            print('El numero de la ruleta es: ' + str(self.numero))
            
    def main(self):
        self.crupier_thread = threading.Thread(target=self.crupier)
        self.crupier_thread.start()
        pool = multiprocessing.Pool(processes=4)
        for i in range(4):
            jugador = Jugador()
            jugador.nombre = names.get_full_name()
            print('Nuevo jugador registrado: ' + jugador.nombre)
            jugador.numero = random.randint(1, 36)
            jugador.saldo = 1000
            pool.apply_async(self.apostar_a_numero, args=(jugador, 10))
        for i in range(4):
            jugador = Jugador()
            jugador.nombre = names.get_full_name()
            print('Nuevo jugador registrado: ' + jugador.nombre)
            jugador.paridad = random.randint(0, 1)
            jugador.saldo = 1000
            pool.apply_async(self.apostar_a_paridad, args=(jugador,))
        for i in range(4):
            jugador = Jugador()
            jugador.nombre = names.get_full_name()
            print('Nuevo jugador registrado: ' + jugador.nombre)
            jugador.numero = random.randint(1, 36)
            jugador.martin_gala += 1
            jugador.saldo = 1000
            pool.apply_async(self.apostar_a_numero, args=(jugador, 10))
        pool.close()
        pool.join()
        self.crupier_thread.join()
        print('\nBalance final: {}'.format(self.casa))

    def main2(self):
        self.crupier_thread = threading.Thread(target=self.crupier)
        self.crupier_thread.start()
        for i in range(4):
            jugador = Jugador()
            jugador.nombre = names.get_full_name()
            print('Nuevo jugador registrado: ' + jugador.nombre)
            jugador.numero = random.randint(1, 36)
            jugador.saldo = 1000
            self.apostar_a_numero(jugador, 10)
        for i in range(4):
            jugador = Jugador()
            jugador.nombre = names.get_full_name()
            print('Nuevo jugador registrado: ' + jugador.nombre)
            jugador.paridad = random.randint(0, 1)
            jugador.saldo = 1000
            self.apostar_a_paridad(jugador)
        for i in range(4):
            jugador = Jugador()
            jugador.nombre = names.get_full_name()
            print('Nuevo jugador registrado: ' + jugador.nombre)
            jugador.numero = random.randint(1, 36)
            jugador.martin_gala += 1
            jugador.saldo = 1000
            self.apostar_a_numero(jugador, 10)
        self.crupier_thread.join()
        print('\nBalance final: {}'.format(self.casa))

if __name__ == '__main__':
    casino = Casino()
    casino.main2()
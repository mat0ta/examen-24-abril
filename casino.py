import threading
import multiprocessing
import time
import random
import names


class Jugador():
    def __init__(self):
        self.nombre = ''
        self.id = 0
        self.numero = 0
        self.paridad = 0
        self.saldo = 0
        self.martin_gala = 0
    
    def __str__(self):
        return {'id': self.id, 'nombre': self.nombre, 'numero': self.numero, 'paridad': self.paridad, 'saldo': self.saldo, 'martin_gala': self.martin_gala}


class Casino():
    def __init__(self):
        self.casa = 50000
        self.ruleta = [1, 36]
        self.crupier_wait_time = 3000  # 3 segundos
        self.numero = self.crupier()
        self.jugadores = []

    def apostar_a_numero(self, jugador, apuesta):
        if jugador.martin_gala > 0:
            apuesta = apuesta * jugador.martin_gala
        jugador.saldo -= apuesta
        if self.casa >= apuesta * 35:
            if self.numero == jugador.numero:
                jugador.saldo += apuesta * 36
                for i in self.jugadores:
                    if i['id'] == jugador.id:
                        i['saldo'] = jugador.saldo
                print(f'El jugador {jugador.nombre} ha ganado  ' + str(apuesta * 36) + '  euros apostando al numero ' + str(jugador.numero) + '. Balance actual: ' + str(jugador.saldo) + ' euros')
            else:
                print(f'El jugador {jugador.nombre} ha perdido ' + str(apuesta) + ' euros apostando al numero ' + str(jugador.numero) + '. Balance actual: ' + str(jugador.saldo) + ' euros')
        else:
            print('La banca no tiene suficiente dinero para pagar la apuesta')

    def apostar_a_paridad(self, jugador):
        jugador.saldo -= 10
        paridad = ''
        if jugador.paridad == 0:
            paridad = 'Par'
        else:
            paridad = 'Impar'
        if self.casa >= 10:
            if self.numero % 2 == jugador.paridad:
                jugador.saldo += 20
                for i in self.jugadores:
                    if i['id'] == jugador.id:
                        i['saldo'] = jugador.saldo
                print(f'El jugador {jugador.nombre} ha ganado 20 euros apostando a numero ' + str(paridad) + f'. Balance actual: {jugador.saldo} euros')
            else:
                print(f'El jugador {jugador.nombre} ha perdido 10 euros apostando a numero ' + str(paridad) + f'. Balance actual: {jugador.saldo} euros')
        else:
            print('La banca no tiene suficiente dinero para pagar la apuesta')

    def crupier(self):
        self.numero = random.randint(0, 36)
        print('El numero de la ruleta es: ' + str(self.numero))
        return self.numero

    def crear_jugador(self, id, martin_gala=0):
        jugador = Jugador()
        jugador.id = id
        jugador.nombre = names.get_first_name()
        jugador.numero = random.randint(1, 36)
        jugador.paridad = random.randint(0, 1)
        jugador.martin_gala = martin_gala
        jugador.saldo = 1000
        return jugador

    def main(self):
        pool = multiprocessing.Pool(processes=4)
        count_id = 0
        for i in range(4):
            jugador = self.crear_jugador(count_id)
            count_id += 1
            self.jugadores.append(jugador.__str__())
            pool.apply_async(self.apostar_a_numero, args=(jugador, 10,))
        for i in range(4):
            jugador = self.crear_jugador(count_id)
            count_id += 1
            self.jugadores.append(jugador.__str__())
            pool.apply_async(self.apostar_a_paridad, args=(jugador,))
        for i in range(4):
            jugador = self.crear_jugador(count_id, 1)
            count_id += 1
            self.jugadores.append(jugador.__str__())
            pool.apply_async(self.apostar_a_numero, args=(jugador, 10,))
        pool.close()
        pool.join()
        balance_j_total = 0
        for i in self.jugadores:
            balance_j_total += i['saldo']
        balance_j_exacto = 1000 * 12 - balance_j_total
        self.casa -= balance_j_exacto
        print('\nBalance final: {}'.format(self.casa))

if __name__ == '__main__':
    casino = Casino()
    casino.main()
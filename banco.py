import threading

class Banco():
    def __init__(self):
        self.balance = 100

    def retirar(self, amount):
        self.balance -= amount
    
    def depositar(self, amount):
        self.balance += amount

    def main(self):
        for i in range(40):
            print("Deposito de 100")
            hilo = threading.Thread(target=self.depositar, args=(100,))
            hilo.start()
        for i in range(20):
            print("Deposito de 50")
            hilo = threading.Thread(target=self.depositar, args=(50,))
            hilo.start()
        for i in range(60):
            print("Deposito de 20")
            hilo = threading.Thread(target=self.depositar, args=(20,))
            hilo.start()
        for i in range(40):
            print("Retirada de 100")
            hilo = threading.Thread(target=self.retirar, args=(100,))
            hilo.start()
        for i in range(20):
            print("Retirada de 50")
            hilo = threading.Thread(target=self.retirar, args=(50,))
            hilo.start()
        for i in range(60):
            print("Retirada de 20")
            hilo = threading.Thread(target=self.retirar, args=(20,))
            hilo.start()
        print('\nBalance final: {}'.format(self.balance))

if __name__ == "__main__":
    banco = Banco()
    banco.main()
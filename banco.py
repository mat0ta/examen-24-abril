import multiprocessing

class Banco():
    def __init__(self):
        self.balance = 100

    def retirar(self, amount):
        self.balance -= amount
    
    def depositar(self, amount):
        self.balance += amount

    def main(self):
        pool = multiprocessing.Pool(processes=4)
        for i in range(40):
            print("Deposito de 100")
            pool.apply_async(self.depositar, args=(100,))
        for i in range(20):
            print("Deposito de 50")
            pool.apply_async(self.depositar, args=(50,))
        for i in range(60):
            print("Deposito de 20")
            pool.apply_async(self.depositar, args=(20,))
        for i in range(40):
            print("Retirada de 100")
            pool.apply_async(self.retirar, args=(100,))
        for i in range(20):
            print("Retirada de 50")
            pool.apply_async(self.retirar, args=(50,))
        for i in range(60):
            print("Retirada de 20")
            pool.apply_async(self.retirar, args=(20,))
        pool.close()
        pool.join()
        print('\nBalance final: {}'.format(self.balance))

if __name__ == '__main__':
    banco = Banco()
    banco.main()
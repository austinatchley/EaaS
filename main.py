
from EaaS import EaaS

class App():
    def __init__(self):
        self.eaas = EaaS()

    def run(self):
        self.eaas.create_test("first")
        self.eaas.run()
        

if __name__ == '__main__':
    app = App()
    app.run()

import requests

class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dadosObtidos = False   

    def obter_todos_os_dados(self):
        resposta = requests.get('')

        if resposta.ok:
            self.dadosObtidos = True
            return 'CONECTADO'
        else:
            self.dadosObtidos = False
            return '404'
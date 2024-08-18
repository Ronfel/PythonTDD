import unittest
from Pessoa import Pessoa

class TestePessoa(unittest.TestCase):
    def setUp(self):
        self.pessoa = Pessoa('Luiz', 'Otavio')

    def teste_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa.nome, 'Luiz')

    def teste_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa.sobrenome, 'Otavio')        

    def teste_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertFalse(self.pessoa.dadosObtidos)            

if __name__ == '__main__':
    unittest.main(verbosity=2)
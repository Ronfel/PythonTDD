import unittest
from Pessoa import Pessoa
from unittest.mock import patch

class TestePessoa(unittest.TestCase):
    def setUp(self):
        self.pessoa = Pessoa('Luiz', 'Otavio')
        self 

    def teste_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa.nome, 'Luiz')

    def teste_pessoa_attr_nome_eh_string(self):
        self.assertIsInstance(self.pessoa.nome, str)        

    def teste_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa.sobrenome, 'Otavio')      

    def teste_pessoa_attr_sobrenome_eh_string(self):
        self.assertIsInstance(self.pessoa.sobrenome, str)               

    def teste_pessoa_attr_dadosObtidos_inicia_falso(self):
        self.assertFalse(self.pessoa.dadosObtidos)         

    def teste_obter_todos_os_dados_sucesso(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa.dadosObtidos)
            

    def teste_obter_todos_os_dados_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.pessoa.obter_todos_os_dados(), '404')
            self.assertFalse(self.pessoa.dadosObtidos)

    def teste_obter_todos_os_dados_sucesso_e_falha(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa.dadosObtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.pessoa.obter_todos_os_dados(), '404')
            self.assertFalse(self.pessoa.dadosObtidos)




if __name__ == '__main__':
    unittest.main(verbosity=2)
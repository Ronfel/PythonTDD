"""
-> Criar Teste
-> Ver o Teste Falhar
=> Ver o Teste Funcionar
-> Melhorar o código.
"""

import unittest
from baconcomovos import bacon_com_ovos

class TesteBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_insertion_error_se_nao_receber_inteiro(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')  # Passando uma string em vez de um inteiro

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multipla_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = "Bacon com ovos"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multipla_3_e_5(self):
        entradas = (1, 2, 4, 7)
        saida = "Passar Fome"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)


    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multipla_3(self):
        entradas = (3, 6, 9, 12)
        saida = "Bacon"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)                


    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multipla_5(self):
        entradas = (5, 10, 20, 25)
        saida = "Ovos"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)                   
                 


unittest.main(verbosity=True)


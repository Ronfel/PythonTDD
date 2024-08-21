import unittest
from src.calculadora import soma

class TesteCalculadora(unittest.TestCase):
    def teste_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5),10,'A soma 5 e 5 não eh igual a 10') 

    def teste_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5,5),0,'A soma -5 e 5 não eh igual a 0') 

    def teste_soma_varias_entradas(self):
        x_y_saidas = (
            (10,10,20),
            (-5,10,5),
            (1.5,1.6,3.1),
            (-5,5,0),
            (100,10,110),
        )


        print('')            
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida                
                self.assertEqual(soma(x,y),saida) 

        
                        

if __name__ == '__main__':
    unittest.main(verbosity=2)
# Etapa 3 – Corrigir o bug e fazer com que os testes passem.

#Atualize a função str_to_bool() para reatribuir a variável value para minúscula usando value.lower(). 

import unittest
    
def str_to_bool(value):
    value = value.lower()
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
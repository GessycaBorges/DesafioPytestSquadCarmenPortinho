# Etapa 1 – Adicionar um arquivo a este exercício.

# Usando as convenções de nome de arquivo do Python para arquivos de teste, crie um novo arquivo de teste. 
# Nomeie o arquivo de teste test_exercise.py e adicione o seguinte código:

import unittest
    
def str_to_bool(value):
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


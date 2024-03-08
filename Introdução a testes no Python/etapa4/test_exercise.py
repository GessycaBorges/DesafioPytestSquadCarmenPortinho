# Etapa 4 – Adicionar novo código com testes.

# Atualize a função para que ela gere um AttributeError se um valor com tipo diferente de cadeia de caracteres for usado. 
# Essa capitalização pode ser detectada capturando um AttributeError ao chamar value.lower() porque apenas as cadeias de caracteres têm um método lower().

# Use um novo método de asserção de unittest.TestCase na classe de teste. 
# Esse novo teste deve verificar se AttributeError é gerado pela entrada não cadeia de caracteres.

import unittest
    
def str_to_bool(value):
    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")
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

    def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1)
            
if __name__ == '__main__':
    unittest.main()
    



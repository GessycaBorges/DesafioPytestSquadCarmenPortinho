# Neste ponto, você deve ter um arquivo de teste de Python chamado test_exercise.py ou algo similar, com os seguintes componentes:

# Uma função str_to_bool()
# Um bloco try/except na função str_to_bool() que captura AttributeError.
# Uma classe de teste TestStrToBool() que herda de unittest.TestCase.
# Pelo menos três métodos de teste que testam entradas para a função str_to_bool().

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
    
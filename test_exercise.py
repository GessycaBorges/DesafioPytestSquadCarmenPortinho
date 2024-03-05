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

class TestAccounts(unittest.TestCase):

    def test_creation(self):
        self.assertTrue(account.create())

    def test_deletion(self):
        self.assertTrue(account.delete())

import unittest

class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
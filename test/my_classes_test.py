
import unittest

from my_lambdata_1.my_utilities import MyDataSplitter
from my_lambdata_1.my_utilities import train_validation_test_split

class TestMyMod(unittest.TestCase):

    def test_train_validation_test_split(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
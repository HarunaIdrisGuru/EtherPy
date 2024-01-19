import unittest
from etherPy.web3 import EtherPy
from etherPy.utils import format_balance

class TestEtherPy(unittest.TestCase):
    def test_get_balance(self):
        etherpy = EtherPy("http://etherpy.com/api")
        balance = etherpy.get_balance("0x123abc")

        self.assertEqual(format_balance(balance), "10 ETH")

if __name__ == "__main__":
    unittest.main()

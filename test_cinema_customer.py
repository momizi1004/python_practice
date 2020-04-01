import unittest

from Customer import customer
from customers import Customers


class TestCinemaCustomer(unittest.TestCase):
    def test_フルネームを取得できる(self):
        with self.subTest("和名"):
            self.assertEqual("Ken Tanaka", customer("Ken", "Tanaka", 15).full_name())

        with self.subTest("英名"):
            self.assertEqual("Tom Ford", customer("Tom", "Ford", 53).full_name())

    def test_顧客の入場料金がわかる(self):
        with self.subTest("20歳未満 1000円"):
            self.assertEqual(1000, customer("Ken", "Tanaka", 15).entry_fee())

        with self.subTest("20歳以上65歳未満は 1500円"):
            self.assertEqual(1500, customer("Tom", "Ford", 53).entry_fee())

        with self.subTest("65歳以上は 1200円"):
            self.assertEqual(1200, customer("Ieyasu", "Tokugawa", 73).entry_fee())

    def test_顧客の情報をCSVで取得できる(self):
        customers = Customers()

        customers.add(customer("Ken", "Tanaka", 15))
        customers.add(customer("Tom", "Ford", 53))
        customers.add(customer("Ieyasu", "Tokugawa", 73))

        expected = "Ken Tanaka,15,1000\n" \
                   "Tom Ford,53,1500\n" \
                   "Ieyasu Tokugawa,73,1200"

        self.assertEqual(expected, customers.info_csv())

    def test_単一の顧客の情報をCSVで取得できる(self):
        Customer = customer("Ken", "Tanaka", 15)

        self.assertEqual("Ken Tanaka,15,1000", Customer.info_csv())


if __name__ == "__main__":
    unittest.main()

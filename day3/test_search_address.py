import unittest

from day3.address_search import AddressSearcher


class TestAddressSearch(unittest.TestCase):
    def setUp(self):
        self.address_searcher = AddressSearcher()

    def test_地名をいい感じで取得できる(self):
        self.assertEqual("岩手県八幡平市大更", self.address_searcher.search(postal_code="0287111"))

    def test_存在しない郵便番号への対応(self):
        self.assertEqual("該当するデータは見つかりませんでした｡検索キーワードを変えて再検索してください｡",
                         self.address_searcher.search(postal_code="0287119"))

    def test_桁数が不正の場合の対応(self):
        print(self.address_searcher.search(postal_code="02871110287111"))
        self.assertEqual("パラメータ「郵便番号」の桁数が不正です。", self.address_searcher.search(postal_code="02871110287111"))

    def test_空文字入力の場合(self):
        self.assertEqual("必須パラメータが指定されていません。", self.address_searcher.search(postal_code=""))


if __name__ == "__main__":
    unittest.main()

from day3.address_search import AddressSearcher


def main():
    postal_code = input("郵便番号(7ケタ)?: ")

    address_searcher = AddressSearcher()

    address_info = address_searcher.search(postal_code)

    print(address_info)


if __name__ == "__main__":
    main()

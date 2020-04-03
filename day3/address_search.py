from day3.my_response import MyResponse


class AddressSearcher:
    def __init__(self):
        self.base_url = "http://zipcloud.ibsnet.co.jp/api/search"

    def search(self, postal_code):
        response = self.make_response(postal_code)

        if response.status != 200:
            return response.message

        if response.results is None:
            return "該当するデータは見つかりませんでした｡検索キーワードを変えて再検索してください｡"

        return response.address_info()

    def make_response(self, postal_code):
        url = f"{self.base_url}?zipcode={postal_code}"

        return MyResponse(url)

    def address_info(self, response):
        都道府県 = response["results"][0]["address1"]
        市区町村 = response["results"][0]["address2"]
        町域 = response["results"][0]["address3"]

        return f"{都道府県}{市区町村}{町域}"

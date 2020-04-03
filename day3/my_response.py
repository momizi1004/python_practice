import requests


class MyResponse:
    def __init__(self, url):
        response = requests.get(url).json()

        self.message = response["message"]
        self.results = response["results"]
        self.status = response["status"]

    def address_info(self):
        address1 = self.results[0]["address1"]
        address2 = self.results[0]["address2"]
        address3 = self.results[0]["address3"]

        return f"{address1}{address2}{address3}"

class Customers:
    def __init__(self):
        self.customer_list = []

    def add(self, customer):
        self.customer_list.append(customer)

    def info_csv(self):
        csvs = [customer.info_csv() for customer in self.customer_list]

        return "\n".join(csvs)

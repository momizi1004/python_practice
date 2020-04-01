class customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.is_child():
            return 1000

        if self.is_adult():
            return 1500

        if self.is_senior():
            return 1200

    def is_child(self):
        return 0 <= self.age < 20

    def is_adult(self):
        return 20 <= self.age < 65

    def is_senior(self):
        return 65 <= self.age

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

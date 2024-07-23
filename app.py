class Employee:

    annual_raise = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@company.com"

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay *= self.annual_raise

    @classmethod
    def set_annual_raise(cls, value):
        cls.annual_raise = value

    @classmethod
    def create_from_string(cls, string):
        first_name, last_name, pay = string.split("-")
        return cls(first_name=first_name, last_name=last_name, pay=pay)

    @staticmethod
    def is_workday(day):
        return False if day.weekday() in (5,6) else True


    def __repr__(self):
        pass

    def __str__(self):
        pass

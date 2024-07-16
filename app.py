# from datetime import datetime, date
# class Employee:
#
#     annual_raise = 1.05
#
#     def __init__(self, first_name, last_name, pay):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.pay = pay
#         self.email = f"{first_name}.{last_name}@company.com"
#
#     def get_fullname(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def apply_raise(self):
#         self.pay *= self.annual_raise
#
#     @classmethod
#     def set_annual_raise(cls, value):
#         cls.annual_raise = value
#
#     @classmethod
#     def create_from_string(cls, string):
#         first_name, last_name, pay = string.split("-")
#         return cls(first_name=first_name, last_name=last_name, pay=pay)
#
#     @staticmethod
#     def is_workday(day):
#         return False if day.weekday() in (5,6) else True
#
# employee1 = Employee(
#     first_name="David",
#     last_name="Smith",
#     pay=10000
# )
#
# print(employee1.pay)
# employee1.apply_raise()
# print(employee1.pay)
#
# employee1.set_annual_raise(value=1.06)
# print(employee1.annual_raise)
# Employee.set_annual_raise(value=1.07)
# print(employee1.annual_raise)
#
# employee2 = Employee(
#     first_name="Test",
#     last_name="User",
#     pay=10000
# )
#
# print(employee2.annual_raise)
#
# employee3_string = "Maria-Doe-2000"
# employee3 = Employee.create_from_string(string=employee3_string)
# print(employee3.email)
# print(employee3.pay)
#
# print(Employee.is_workday(datetime.now()))
# print(Employee.is_workday(date(2024, 7, 6)))
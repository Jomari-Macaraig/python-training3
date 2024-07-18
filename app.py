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
#
# class Developer(Employee):
#     pass
#
# developer = Developer(first_name="Jomari", last_name="Macaraig", pay=1000)
# print(developer.email)
#
# print(help(developer))
#
# print(developer.pay)
# developer.apply_raise()
# print(developer.pay)
#
#
# class Developer(Employee):
#     annual_raise =  1.10
#
# developer = Developer(first_name="Jomari", last_name="Macaraig", pay=1000)
#
# print(developer.pay)
# developer.apply_raise()
# print(developer.pay)
#
#
# class Developer(Employee):
#
#     def __init__(self, first_name, last_name, pay, programming_language):
#         self.programming_language = programming_language
#         super().__init__(first_name=first_name, last_name=last_name, pay=pay)
#
# developer1 = Developer(first_name="Jomari", last_name="Macaraig", pay=1000, programming_language="Python")
# developer2 = Developer(first_name="John", last_name="Doe", pay=1000, programming_language="Java")
#
# print(developer1.email)
# print(developer1.programming_language)
#
# print(developer2.email)
# print(developer2.programming_language)
#
#
# # Exercise
# """
#     Create a Manager class that subclass Employee class. A manager manage people or employees thus this class should
#     accept an optional parameter called employees. If no employee passed, set it to an empty list
# """
#
#
#
#
#
#
#
#
#
#
#
#
# class Manager(Employee):
#
#     def __init__(self, first_name, last_name, pay, employees=None):
#         super().__init__(first_name=first_name, last_name=last_name, pay=pay)
#         self.employees = employees or []
#
#     def add_employee(self, employee):
#         if employee not in self.employees:
#             self.employees.append(employee)
#
#     def remove_employee(self, employee):
#         if employee in self.employees:
#             self.employees.remove(employee)
#
#     def print_employees(self):
#         for employee in self.employees:
#             print(f"---> {employee.get_fullname()}")
#
# manager = Manager(first_name="Dennis", last_name="Guzman", pay=1001, employees=[developer1])
# print(manager.email)
# print(manager.print_employees())
# manager.add_employee(developer2)
# print(manager.print_employees())
# manager.add_employee(developer1)
# print(manager.print_employees())
#
#
# print(isinstance(manager, Employee))
# print(isinstance(manager, Developer))
#
# print(issubclass(manager, Employee))
# print(issubclass(manager, Developer))
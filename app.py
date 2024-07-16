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

    # def apply_raise(self):
    #     self.pay *= 1.05

    # def apply_raise(self):
    #     self.pay *= self.annual_raise

    # def apply_raise(self):
    #     self.pay *= Employee.annual_raise


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
# employee1.annual_raise = 1.06
# Employee.annual_raise = 1.06
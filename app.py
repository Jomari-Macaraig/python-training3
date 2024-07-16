# class SingletonClass:
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "instance"):
#             cls.instance = super(SingletonClass, cls).__new__(cls)
#         return cls.instance
#
# singleton = SingletonClass()
# new_singleton = SingletonClass()
#
# print(singleton is new_singleton)
# print(singleton)
# print(new_singleton)
#
# singleton.instance_variable = "Instance Variable"
# print(new_singleton.instance_variable)
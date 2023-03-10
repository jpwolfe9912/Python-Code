# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234")
# ]

# username_mapping = {user[1]: user for user in users}

# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

# _, username, password = username_mapping[username_input]
# if password_input == password:
#     print("Welcome")
# else:
#     print("Failed")

# def multiply(*args):
#     prod = 1
#     for i in args:
#         prod *= i

#     return prod

# print(multiply(10,2,3))

# def named(**kwargs):
#     print(kwargs)

# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")

# print_nicely(name="Bob", age=25)

# class Student:
#     def __init__(self):
#         self.name = "Rolf"
#         self.grades = (90, 85, 88, 82, 97)

#     def average(self):
#         return sum(self.grades) / len(self.grades)

# student = Student()
# print(student.average())

class ClassTest:
    def instance_method(self):
        print(f"Called method of {self}")

test = ClassTest()
print(test.instance_method())
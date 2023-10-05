# class Employees:
#     def __init__(self, name, last) -> None:
#         self.name = name
#         self.last = last


# class Supervisors(Employees):
#     def __init__(self, name, last, password) -> None:
#         super().__init__(name, last)
#         self.password = password


# class Chefs(Employees):
#     def leave_request(self, days):
#         return "May I take a leave for " + str(days) + " days"

# adrian = Supervisors("Adrian", "A", "apple")

# emily = Chefs("Emily", "E")
# juno = Chefs("Juno", "J")

# print(emily.leave_request(3))
# print(adrian.password)
# print(emily.name)

# from math import pi

# print(math.pi)

# names = ["Brian", "Tom", "Jim"]
# names.insert(2, "Amy")
# print(names)

# simple_dict = {1: "Coffee", 2: "Tea", 3: "Juice"}
# for x in simple_dict:
#     print(x)


def d():
    color = "green"

    def e():
        nonlocal color
        color = "yellow"

    e()
    print("Color: " + color)
    color = "red"


color = "blue"
d()

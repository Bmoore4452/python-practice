# import time

# start_time = time.time()
# http_status = int(input("Enter HTTP status code:\n200\n400\n500\n"))

# match http_status:
#     case 200 | 201:
#         print("Success")
#     case 400:
#         print("Bad Request")
#     case 404:
#         print("Not Found")
#     case 500 | 501:
#         print("Server Error")
#     case _:
#         print("Unknown")

# print(round((time.time() - start_time), 2))

# a = isinstance(str, "a")

# print(a)

# menu = {
#     1: {"name": "espresso", "price": 1.99},
#     2: {"name": "coffee", "price": 2.50},
#     3: {"name": "cake", "price": 2.79},
#     4: {"name": "soup", "price": 4.50},
#     5: {"name": "sandwich", "price": 4.99},
# }

# list1 = ["cake", "soup", "sandwich"]
# subtotal = 0
# # print(menu[1]["name"])
# print(type(menu))
# for i in menu:
#     for j in list1:
#         if menu[i]["name"] == j:
#             subtotal += menu[i]["price"]
# print(round((subtotal), 2))
# # if menu[i + 1] == i + 1:
# #     print(menu[i + 1]["name"])


# def change(array, modulus):
#     return x[::-1][:modulus] + x[modulus:]
# array1 = [1, 3, 5, 7, 9, 11]
# modulus1 = 3
# change(array1, modulus1)

a = [[96], [69]]
print("".join(list(map(str, a))))

# def is_positive(n):
#     return n > 0

# def get_positive_int():
#     age = int(input("Age: "))
#     while not is_positive(age):
#         age = int(input("Age must be positive. Age: "))
#     return age

# def get_non_empty_string():
#     name = input("Name: ")

#     while name == "":
#         name = input("Name can't be empty. Name: ")

#     return name

# def main():
#     age = get_positive_int()
#     name = get_non_empty_string()

#     print(name, age)

# main()




# # def count_even(numbers):
# #     count = 0
# #     for num in numbers:
# #         if num % 2 == 0:
# #             count += 1
# #     return count
# # nums = [2, 1, 6, 8]
# # print(count_even(nums))


# # def add_prefix(names, prefix):
# #     for name in names:
# #         return name.append(prefix)
    
# # names = ["Tosin", "Mary"]
# # print(add_prefix(names, "Dr"))


# # def add_prefix(names, prefix):
# #     new_list = []
# #     for name in names:
# #         new_list.append(prefix + name)
# #     return new_list
# # names = ["Tosin", "Mary"]
# # print(add_prefix(names, "Dr. "))


# def count_even(numbers):
#     count = 0
#     for num in numbers:
#         if num % 2 == 0:
#               count +=1
#     return count
# numbers = [1,4,8,3]

# print(count_even(numbers))


# def add_prefix(names, prefix):
#      new_list = []
#      for name in names:
#           new_list.append(prefix + name)
#      return new_list
# names = ["Tosin", "Mary"]
# print(add_prefix(names, "Dr. "))

# def is_integer(n):
#      return n == int

# def get_price():
#      price = float(input("Price: "))
#      while not is_integer(price):
#           price = float(input("Price must be a number. Price: "))
#      return price

# def get_quantity():
#      qty = int(input("Quantity: "))
#      while not is_integer(qty):
#           price = float(input("Qty must be a number. Quantity: "))
#      return qty

# def get_total(total, qty):
#      total = get_price + get_quantity
#      if total >= 100:
#           total = total * 0.9
#      return total


# def main(total, qty):
#     total = get_total()
#     qty = get_quantity()

#     return (total, qty)

# print(f'Total is {main}')
     


# def get_price():
#     return float(input("Price: "))

# def get_quantity():
#     return int(input("Quantity: "))

# def calculate_total(price, qty):
#     total = price * qty
#     if total >= 100:
#         total *= 0.9
#     return total

# def main():
#     price = get_price()
#     qty = get_quantity()
#     total = calculate_total(price, qty)
#     print("Total:", total)

# main()

# def calculate_total(price, qty):
#     total = price * qty
#     if total >= 100:
#         total *= 0.9
#     return total

# def main():
#     price = float(input("Price: "))
#     qty = int(input("Quantity: "))
#     total = calculate_total(price, qty)
#     print("Total:", total)

def average_numbers(numbers):
    return sum(numbers) /len(numbers)
   

numbers = [2,4,6,8,10]
print(average_numbers(numbers))



def  count_above (numbers, threshold = 2):
    threshold_count = 0
    for num in numbers:
        if num > threshold:
            threshold_count += 1
    return threshold_count

numbers = [2,1,6,8]
print(count_above(numbers))



def average_maximun(numbers):
    new_list = []
    for num in numbers:
        new_list.append(num / max(numbers))
    return new_list
numbers = [2,4,6,8,2]
print(average_maximun(numbers))

def normalize(numbers):
    max_value = max(numbers)
    new_list = []
    for num in numbers:
        new_list.append(num / max_value)
    return new_list

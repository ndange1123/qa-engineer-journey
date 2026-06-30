# # Print you Introduction
# print('''Hello! My name is Nitin Dange, I am senior software engineer working with MNC.
# my passion is coding and problem solving, i enjoy learning and reading books. my Favorite book it "Atomic Habits"
# ''')
#
# # swap two numbers
# a = 5
# b = 10
# c = b
# b = a
# a = c
#
# print(f"After swap a is {a} and b is {b}")
#
# # check whether a number is even or odd
#
# def even_odd(num):
#     if type(num) != int :
#         return print("Enter valid Number")
#     if num % 2 == 0:
#         print(f"Entered Number {num} is even number")
#     else:
#         print(f"Entered Number {num} is ODD number")
#
# even_odd("12333")
#
# # Find the largest of three numbers
#
# def largest_number(num1, num2, num3):
#     if (type(num1) or type(num2) or type(num3)) != int:
#         print('Enter valid numbers for comparison')
#
#     largest = num1
#
#     if num2 > largest:
#         largest = num2
#
#     if num3 > largest:
#         largest = num3
#
#     print(f"Largest number among three number is {largest}")
#
# largest_number(13,32,9)
#
#
# #reverse a string
#
# def reverse_string(enter_string):
#     reverse = ""
#     for char in enter_string:
#         reverse = char + reverse
#     print("Reversed string:", reverse)
#
# reverse_string("Hello World!")
#
# ## reverse a string
#
# def reverseString_simple(enter_string):
#     result = enter_string[::-1]
#     return result
#
# result = reverseString_simple("i am Hello World!")
# print(f"Simple reverse string is : {result}")
#
#
# ### count vowels in a string
# def count_vowels(enter_string):
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     count = 0
#     enter_string = enter_string.lower()
#     for char in enter_string:
#         if char in vowels:
#             count = count + 1
#     return count
#
# result = count_vowels("hello World!")
# print(result)
#
#
# ## Factorial of number using loop
#
# def factorial(number):
#     if number < 0:
#         return None
#     if type(number) != int:
#         return None
#
#     fact = 1
#     while number > 0:
#         fact = fact * number
#         number -= 1
#     return fact
#
# print(factorial(7))

## print fibonacci series

def fibonacci(number):
    f0 = 0
    f1 = 1
    print(f0, f1, end=" ")
    for i in range(2, number):
        fn = f0 + f1
        print(fn, end=" ")
        f0 = f1
        f1 = fn

fibonacci(20)


# remove duplicates from list

def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result

print(remove_duplicates([1, 2, 2, 3, 2, 8,4,5,6,6,4]))
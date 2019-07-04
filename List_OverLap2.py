# import random
# numbers_1 = int(input("Highest List Number in List 1: "))
# # numbers_2 = int(input("Highest List Number in List 2: "))

# num1 = range(numbers_1)


# # # for x in range(numbers_1):
# # #         for y in range(numbers_2):
# # #                 c = x + y
# # #                 print(random.randint(0, c))              

# # # generate range of numbers
# # num1 = range(0, numbers_1)
# # num2 = range(0, numbers_2)

# # #go through each number in each list and output it to i and x. 
# # for i in num1:
# #         for x in num2:
# #                 y = set(x) & set(i) 
# #                 print(y)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for num in a:
        if num in b:
                print(num)


# c = set(a) & set(b)
# print(c)

# for item in range(0,100):
#         print(random.randrange(0,100))        
# # d = random.randrange(0, 100)
# print(d)
# e = random.randrange(0, 50)

# f = set(d) & set(e)
# print(f)
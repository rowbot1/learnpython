import random
numbers_1 = (int(input("List 1 size: ")))
numbers_2 = (int(input("List 2 size: ")))


for n1 in range(numbers_1):
    x = (random.randint(0 , n1))
    print(x)
    for n2 in range(numbers_2):
            y = (random.randint(0, n2))
            c = x + y

unique_list = set(c)
print(unique_list)
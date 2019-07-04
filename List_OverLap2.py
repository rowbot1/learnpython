import random
numbers_1 = int(input("List 1 size: "))
numbers_2 = int(input("List 2 size: "))

#take user input and generate a range
for n1 in range(numbers_1):
    x = random.randint(0 , n1)
    
    for n2 in range(numbers_2):
        y = random.randint(0, n2)
        c = x + y

my_set = set(c)
my_new = list(c)
# unique_list = set(c)
print(my_new)
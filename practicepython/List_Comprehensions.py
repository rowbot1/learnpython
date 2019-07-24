"""
https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

https://youtu.be/3dt4OGnU5sM?t=206"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# first 'n' is what i want - always declare this first, 2nd 'n' is part of the for loop.
even = [number for number in a if number % 2 == 0]
print(even)

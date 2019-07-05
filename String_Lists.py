word = input("Enter Word: ")
# print(word[:])

#could use a reverse function or something - dont think thats the intended way

#put every letter noonin word in reverse order, then compare it to word variable, if same then print true

# get length of word
# add end letter to list
# add next letter to list
# add first letter to list
# compare list to word variable 

# for letter in word:
#     backwards_word = word[:-1]
#     print(backwards_word)
    
# i = len(word)
# j = i+1
# print(i)

letter = word[::-1] 
print(letter, end= ' ' )  

if word == letter:
    print(True)
else:
    print(False)

# print(i)

# while i >=0:
#     print(word[i])
#     i -= 1



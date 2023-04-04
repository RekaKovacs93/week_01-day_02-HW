# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:


# 2. Print the difference between the largest and smallest value:


# 3. Print True if the list contains a 2 next to a 2 somewhere.


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 


for num in numbers :
    if num % 2 == 0 :
        print(num)

# numbers.sort()
# print(numbers[9] - numbers[0])

for i in numbers :
    if i == 2 & i + 1 == 2:
        print(True)
        break

total = 0
# for num in numbers :
#     if num == 6 :
#         while num != 7 :
#             total = 0
#     else :
#         total += num
# print(total)

# while num in numbers != 6:
#     total += num
# print(total)

ind = numbers.index(13)
negate = 13 + numbers[ind+1]
for num in numbers:
    total += num
print(total - negate)
    

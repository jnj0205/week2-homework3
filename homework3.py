#Exercise 1    
#Given an array of positive integers nums, return a list of all of the negative integers.
#Ex. 1
#nums = [1, 3, 5, 7, 8]
#Expected Output: [-1, -3, -5, -7, -8]


def negative_numbers (nums):
    answer = []
    for num in nums:
        answer.append(num * (-1))
    return answer
print(negative_numbers ([1, 2, 3, 4, 5]))


#print(negative_numbers([100, 534, 32, 15, 77, 222, 788, 345, 75645, 22]))




##Exercise 2#########
###
#Given a string, return a list of all of the digits in the string.
#Ex. 1

#Expected Output: ['1', '2', '3', '2', '4', '3', '4', '9', '8']

#Ex. 2
#sentence = "My phone number is (555) 555-4321"
#Expected Output: ['5', '5', '5', '5', '5', '5', '4', '3', '2', '1']
#
address = "123 Real Street, Apt. 2, Springfield, OR 43498" 

def only_number(address):
    return [i for i in address if i.isdigit()]        
result = only_number(address)
print(result)
 ###
  ##Given a string digits, return a string of the digits + 1

##Ex. 1
#digits = '123'
#Expected Output: '124'
def f(x):
    return str(int(x) + 1)
y = f('123')
print(str(y))


#Ex. 2
#digits = '99'
#Expected Output: '100'

def f(x):
    return str(int(x) + 1)
y = f('99')
print(str(y))

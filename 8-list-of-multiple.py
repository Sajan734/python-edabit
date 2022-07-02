# Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.

def list_of_multiples(num, length):
    numlist = [num]
    while num * length > numlist[-1]:
        numlist.append(numlist[-1] + num)
    return numlist

print(list_of_multiples(17, 6))
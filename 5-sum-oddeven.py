# Write a function that takes a list of numbers and returns a list with two elements:

# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.

def sum_odd_and_even(numlist):
    even = []
    odd = []
    final = []
    i = 0
    while i < len(numlist):
        if numlist[i] % 2 == 0:
            even.append(numlist[i])
        else:
            odd.append(numlist[i])
        i += 1

    final.append(sum(even))
    final.append(sum(odd))
    print(final)
    return(final)

sum_odd_and_even([0, 0])
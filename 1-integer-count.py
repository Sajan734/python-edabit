# Create a function that takes a number num and returns its length. (No using len())

def countInteger(num):
    count = 0
    while num >= 1:
        num = num / 10
        count = count + 1
    print(count)
    # return count
        
num = int(input('Number: '))
countInteger(num)


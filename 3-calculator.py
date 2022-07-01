# input: 1 + 2 --> output: 3
# input: 6 / 2 --> output: 3
# input: 10 / 2 --> output: 5
# input: 5 * 2 --> output: 10
# input: 10 - 5 --> output: 5

def calculator(eq):
    nums = eq.split()
    a = nums[0]
    b = nums[2]
    op = nums[1]
    operators = ['+','-','*','/']
    if op == operators[0]:
        print(int(a) + int(b))
        # return a + b
    if op == operators[1]:
        print(int(a) - int(b))
        # return a - b
    if op == operators[2]:
        print(int(a) * int(b))
        # return a * b
    if op == operators[3]:
        print(int(a) / int(b))
        # return a / b

eq = input('Question: ')
calculator(eq)

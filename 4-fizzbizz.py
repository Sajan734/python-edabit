def fizzbizz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBizz')
        return 'FizzBizz'
    if num % 3 == 0:
        print('Fizz')
        return 'Fizz'
    if num % 5 == 0:
        print('Bizz')
        return 'Bizz'
    else:
        print(num)
        return num

num = int(input('Number: '))
fizzbizz(num)
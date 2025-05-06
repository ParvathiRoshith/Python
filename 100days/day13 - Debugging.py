#odd even
def odd_or_even(number):
    if number % 2 == 0:
        return 'This is an even number.'
    else:
        return 'The number is odd.'
print(odd_or_even(99))
    
#leap year
def is_leap_year(yr):
    if yr % 4 == 0:
        #return True
        if yr % 100 == 0:
            #return False
            if yr % 400 == 0:
                return True
        else:
            return True
    else:
        return False
print(is_leap_year(1967))
    
#FizzBuzz
def fizz_buzz(x):
    for i in range(1,x+1):
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)
fizz_buzz(15)
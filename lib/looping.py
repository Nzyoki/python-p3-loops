#!/usr/bin/env python3
'Write a function happy_new_year() using a while loop that outputs numbers starting at 10 and counting down to 1. After reaching 1, print out "Happy New Year!"'
def happy_new_year():
    num=10
    while num >=1:
        print (num)
        num -=1
    print('Happy New Year!')
    # code goes here!
    pass
'Write a function square_integers() that takes one argument, a list of integers and returns the list of squared elements.'
def square_integers(int_list):
    return [i **2 for i in int_list]
       # print(i**2)

    # code goes here!
    pass
'''Write a function fizzbuzz() that prints the numbers from 1 to 100. 
For multiples of three, print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five, print "FizzBuzz".'''
def fizzbuzz():
    for i in range(1,101):
        if i%3 ==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)

        
    # code goes here!
    pass

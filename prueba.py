#!/usr/bin/python3
import sys

'''
numbers_lcd: dict{key: numbers, value:[str]
its a dictionary that represents each digit 
in 5 lines format from top to bottom
'-': horizontal line
' ': horizontal empty space
'b': vertical line at both sides
'r': vertical line at right side
'l': vertical line at left side
'''
numbers_lcd = {
    '0': ['-', 'b', ' ', 'b', '-'],
    '1': [' ', 'r', ' ', 'r', ' '],
    '2': ['-', 'r', '-', 'l', '-'],
    '3': ['-', 'r', '-', 'r', '-'],
    '4': [' ', 'b', '-', 'r', ' '],
    '5': ['-', 'l', '-', 'r', '-'],
    '6': ['-', 'l', '-', 'b', '-'],
    '7': ['-', 'r', ' ', 'r', ' '],
    '8': ['-', 'b', '-', 'b', '-'],
    '9': ['-', 'b', '-', 'r', '-']
}


def check_number(numbers: int, size: int):
    '''
    this function prints the number in LCD format.
    let consider numbers = 12345 and size = 2
    then the output will be  
       --   --        --  
    |    |    | |  | |    
    |    |    | |  | |
       --   --   --   --
    | |       |    |    |
    | |       |    |    |
       --   --        --     
    as you can see we devided the number in 5 parts from top down,
    the top the middle and the botton are handle it using, print_columns
    and the other ones with print_rows
    '''
    for i in range(5):
        if i % 2 == 0:
            print_rows(numbers, size, i)
        else:
            print_columns(numbers, size, i)
    print('\n')


def print_columns(numbers: int, size: int, position):
    '''
    let consider the same example, this method is incharge
    of printing the following lines
    ->     --   --        --  
        |    |    | |  | |    
        |    |    | |  | |
    ->     --   --   --   --
        | |       |    |    |
        | |       |    |    |
    ->     --   --        --      
    '''
    for _ in range(size):
        for num in numbers:

            signed = numbers_lcd[num][position]

            if signed == 'b':
                print(f"|{size * ' '}|", end=' ')
            elif signed == 'r':
                print(f" {size * ' '}|", end=' ')
            elif signed == 'l':
                print(f"|{size * ' '} ", end=' ')
        print()


def print_rows(numbers: int, size: int, position):
    '''
    let consider the same example, this method is incharge
    of printing the following lines
           --   --        --  
    ->  |    |    | |  | |    
    ->  |    |    | |  | |
           --   --   --   --
    ->  | |       |    |    |
    ->  | |       |    |    |
           --   --        --      
    '''
    for num in numbers:
        signed = numbers_lcd[num][position] * size
        print(f" {signed} ", end=' ')
    print()


# Driver code
if __name__ == '__main__':
    # Function call to check digit

    flag = False
    while flag is False:
        multiline = []
        while True:
            user_input = input()
            if user_input:
                multiline.append(user_input)
            else:
                break
        lines = " ".join(multiline)
        no_spaces = lines.split(' ')

        stop_program = '0,0'
        for i in no_spaces:
            if i == stop_program:
                flag = True
                break
            size = int(i.split(',')[0])
            numbers = i.split(',')[1]
            if size > 10 or size <= 0:
                print('size goes from 1 to 10')
            else:
                check_number(numbers, int(size))

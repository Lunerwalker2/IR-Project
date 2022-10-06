#!/usr/bin/env python3

#dunder or magic methods double underscore __name__, __init__

#initial python method
def method():
    #pass allows you to skip this line of code
    pass
    #continue allows you to skip an iterator in a loop

#method declaration with parameter not set
def method_2(param1):
    print(param1)

#method declaration with parameter preset
def method_3(param1 = None):
    print(param1)

#two arguments predefined
def method_4(param1 = 0, param2 = 1):
    print('param1', param1)
    print('param2', param2)

#variable argument passing without keys
def method_arg(*arg):
    print(arg)

#variable number of arguments passing with keys
def method_kwarg(**kwarg):
    print(kwarg)

#function/method to demonstrate binary / hex conversions and manipulations
def binary_hex():
    string = 'a'
    #ord = pythons method for converting char to int
    int_value = ord( string[0] ) # should match ASCII table for common char
    print('int_value', int_value)
    #str() python type for strings
    encoded_variable = str.encode(string)
    #encoded variable will return an array/list of bytes
    print( encoded_variable )
    #will provide the first integer value representative of a in ASCII
    print( encoded_variable[0] )
    #decode the string from bytes to string characters
    print( encoded_variable.decode() )
    #type castring a character in python
    print( chr(97) )
    #output the hex value of the integer value
    print( hex(int_value) )
    #output the binary value of the integer value
    print( bin(int_value) )
    #int (what, base) - base 16 = hex
    #manipulating str by passing in base. This is not the same value as above
    print( int(string[0], 16) )
    print( hex( int(string[0], 16) ) )
    #hex = 0-9 A-F 1010

def colon_operator():
    list_variable = [1,2,4,6,7,8,4,2]
    #start:stop:step_size
    #start is inclusive, stop is exclusive
    print( list_variable[0:4] )
    print( list_variable[2:4] )
    print( list_variable[0:4:2] )
    #this uses negative step size to reverse the list
    print( list_variable[-1:-4:-1] )


global_variable = 20
def global_values():
    #global keyword is needed to utilize the globally declared object
    global global_variable
    #reassignment makes the variable a local variable and no longer references it
    print('global_variable before assignment in global_values:', global_variable)
    global_variable = 10 
    print('global_variable from the method global_values:', global_variable)

#lambda function examples
def lambda_functions(n = 2):
    #lambda requires the inputs: output
    doubler = lambda param1: param1 * param1
    print( doubler(2) )
    multiplier = lambda param1, param2: param1 * param2
    print ( multiplier(2, 3) )
    #you can use lambda for many applications including filtering
    filter_even = lambda input_list: input_list % 2 == 0 
    filtered = filter( filter_even, [1,2,3,4,5,6,7,8] )
    print( list(filtered) )
    #you can use return lamdas for enhance cababilities
    return lambda x: x**n
    

def main():
    #main program print
    print('this is out main program')
    #calling methods 1-4
    method()
    method_2(3)
    method_2("this is a string")
    #this causes an error because method_2 requires a parameter
    # method_2()
    #predefining values for your parameter allows you to not pass one in
    method_3()
    method_4()
    method_4(2, 3)
    # method_4(2)
    method_4(param2 = 3)
    #variable argument example * does not require key's
    method_arg(1, 2, 3, 4, 5)
    #variable argument example ** requires keys
    method_kwarg(key_1 = 1, key_2 = 2)
    #kwargs are using in machine passing models and datasets. 

    #binary example call
    binary_hex()

    #global example call
    print('global_variable', global_variable)
    global_values()
    print('global_variable', global_variable)

    #colon operator call
    colon_operator()

    #doubler and tripler based on the return lambda function
    doubler = lambda_functions(n = 2)
    print( doubler(2) )
    tripler = lambda_functions(n = 3)
    print( tripler(2) )

if __name__ == "__main__":
    main()


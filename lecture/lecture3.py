#!/usr/bin/env python3
#https://en.wikipedia.org/wiki/Shebang_(Unix)

#print hello sample
print('hello world')
print("hello' 'world")
#JSON format
print('{"message":"JSON Format"}')
print("{\"message\":\"JSON Format\"}")

#declaring a variable
variable = 10

#redifining sum to be a variable. (Not A Good Practice)
# sum = variable + variable
# print(sum)

#defining variable_2 with bad code practices
# variable_2=[10,25,5,-3] #not proper coding standard

#defining variable_2
variable_2 = [10, 25, 5, -3]
# print(sum(variable_2))

#printing the sum using python built in keyword
print( sum( variable_2 ) )

#This comment is longer than 80 characters. Therefore, you should split the commenting to two line or reduce the size of the comment.

condition_variable = 1

#different ways to check conditionals
# if condition_variable:
# if condition_variable == 1:
# if condition_variable == True:
    # print( 'True' )

#True == anything above a 0 or Flase. Unless you use the == operator.
condition_variable = 2
if condition_variable:
    print( 'True' )

condition_2 = 3

if condition_2 == 2:
    print( 'condition is:', condition_2)
elif condition_2 == 3:                      #ekse if in python is elif 
    print( 'condition is:', condition_2)
else:
    print( 'condition is neither 2 or 3' )

#-----------------------------------------------------------------------------#
# Python Types | Data Structures #
integer_type = 5
float_type = 5.0
string_type = str(5)
#plus additional data structure types including lists, dictionaries, tuples, 
# sets, etc. 

print( type(integer_type) )
print( type(float_type) )
print( type(string_type) )

#you can use type to check if an object is of specific data type.
if type( integer_type ) == type ( int() ):
    print( 'It is an integer' )

#lists() - a collection of object. It does not have to be the same type.
list_variable = [1, 3, 4, 10]
print( type( list_variable ) )

list_variable = [1, "string", 5.0, 4]
print( 'list_variable :', list_variable )

#indexes in python start from 0
print( list_variable[1] )

#2 * provides two times the elements instead of mathematically multiplying
print( 2 * list_variable )

#different ways to define list
list_variable = []
list_variable = list()
#you can add values in the list

# # List Methods
# # append()	Adds an element at the end of the list
# # clear()	Removes all the elements from the list
# # copy()	Returns a copy of the list
# # count()	Returns the number of elements with the specified value
# # extend()	Add the elements of a list (or any iterable), to the end of the current list
# # index()	Returns the index of the first element with the specified value
# # insert()	Adds an element at the specified position
# # pop()	Removes the element at the specified position
# # remove()	Removes the item with the specified value
# # reverse()	Reverses the order of the list
# # sort()	Sorts the list

list_variable = [1, 4, 7]
value_pop = list_variable.pop(1)

print( value_pop )
print( list_variable )

#-----------------------------------------------------------------------------#
#tuples

#defining a tuple
tuple_variable = (2, 3)

#tuples can be converted from lists and backwards
tuple_variable = tuple( [3, 4] )

print(tuple_variable)
print( type( tuple_variable ) )

#unpacking tuples
variable_one, variable_two = tuple_variable

print( 'variable_one:', variable_one )
print( 'variable_two:', variable_two )

#-----------------------------------------------------------------------------#
#dictionaries - use key:value pairs

#defining dictionaries
dictionary_variable = dict()
dictionary_variable = {}
dictionary_variable = { "key_1" : "value_1" }
dictionary_variable = { "key_1" : [1, 5, "value", 4.0] }

print( dictionary_variable )

#you cannot index it by number. You must index by key.
# print( dictionary_variable[0] )
print( dictionary_variable[ 'key_1' ] )

# #Dictonary
# # clear()	Removes all the elements from the dictionary
# # copy()	Returns a copy of the dictionary
# # fromkeys()	Returns a dictionary with the specified keys and value
# # get()	Returns the value of the specified key
# # items()	Returns a list containing a tuple for each key value pair
# # keys()	Returns a list containing the dictionary's keys
# # pop()	Removes the element with the specified key
# # popitem()	Removes the last inserted key-value pair
# # setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# # update()	Updates the dictionary with the specified key-value pairs
# # values()	Returns a list of all the values in the dictionary

print( dictionary_variable.values() )
print( dictionary_variable.keys() )

#-----------------------------------------------------------------------------#
#python sets = cannot have duplicate items. 

set_variable = set()

# #Set Methods
# # add()	Adds an element to the set
# # clear()	Removes all the elements from the set
# # copy()	Returns a copy of the set
# # difference()	Returns a set containing the difference between two or more sets
# # difference_update()	Removes the items in this set that are also included in another, specified set
# # discard()	Remove the specified item
# # intersection()	Returns a set, that is the intersection of two other sets
# # intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# # isdisjoint()	Returns whether two sets have a intersection or not
# # issubset()	Returns whether another set contains this set or not
# # issuperset()	Returns whether this set contains another set or not
# # pop()	Removes an element from the set
# # remove()	Removes the specified element
# # symmetric_difference()	Returns a set with the symmetric differences of two sets
# # symmetric_difference_update()	inserts the symmetric differences from this set and another
# # union()	Return a set containing the union of sets
# # update()	Update the set with the union of this set and others

#pandas - another dataset in python provding data frames

#-----------------------------------------------------------------------------#
#loops 

#range - list of items (indexes)
#range(6)
#range(1, 6)
#range(6)

print( range(6) )
print( range(1, 6) )
print( range(1, 6, 2) )

list_variable = [1, 2, 3, 4, 5, 10]

#using range for the for loop 
for index in range( len(list_variable) ):
    print(index, list_variable[index])

#using the in keyworld to iterate through the items
for item in list_variable:
    print( item )

#enumerate - returns the range count and the item 
for index, item in enumerate(list_variable):
    print(index, item)

#range is inclusive at the start not end.
for index in range(6):
    print(index)

for index in range(1, 6):
    print(index)

#range( start, end, separation)
for even in range(0, 6, 2):
    print(even)

while_conition = 0
while while_conition < 6:
    while_conition += 1
    print(while_conition)
else:
    print('do something when the initial condition is not met')

#-----------------------------------------------------------------------------#
#logic operators
# # Math Comperators
# # ==	Equal	x == y	
# # !=	Not equal	x != y	
# # >	Greater than	x > y	
# # <	Less than	x < y	
# # >=	Greater than or equal to	x >= y	
# # <=	Less than or equal to	x <= y

# # Bitwise Operators
# # & 	AND	Sets each bit to 1 if both bits are 1
# # |	OR	Sets each bit to 1 if one of two bits is 1
# #  ^	XOR	Sets each bit to 1 if only one of two bits is 1
# # ~ 	NOT	Inverts all the bits
# # <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# # >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# #Math Operators
# # +	Addition	x + y	
# # -	Subtraction	x - y	
# # *	Multiplication	x * y	
# # /	Division	x / y	
# # %	Modulus	x % y	
# # **	Exponentiation	x ** y	
# #  //	Floor division	x // y

# # Assignment Operators
# # =	x = 5	x = 5	
# # +=	x += 3	x = x + 3	
# # -=	x -= 3	x = x - 3	
# # *=	x *= 3	x = x * 3	
# # /=	x /= 3	x = x / 3	
# # %=	x %= 3	x = x % 3	
# # //=	x //= 3	x = x // 3	
# # **=	x **= 3	x = x ** 3	
# # &=	x &= 3	x = x & 3	
# # |=	x |= 3	x = x | 3	
# # ^=	x ^= 3	x = x ^ 3	
# # >>=	x >>= 3	x = x >> 3	
# # <<=	x <<= 3	x = x << 3

# # Logical Comperators
# # and 	Returns True if both statements are true	x < 5 and  x < 10	
# # or	Returns True if one of the statements is true	x < 5 or x < 4	
# # not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

variable_one = 4
variable_two = 8
if variable_one > 3 and variable_two < 9:
    print( 'both conditions met' )

# # Identiry Operators
# # is 	Returns True if both variables are the same object	x is y	
# # is not	Returns True if both variables are not the same object	x is not y

# # Membership Operators
# # in 	Returns True if a sequence with the specified value is present in the object	x in y	
# # not in	Returns True if a sequence with the specified value is not present in the object	x not in y


list_variable = [1, 4, 5, 7, 10]

if 10 in list_variable:
    print( 'Item exists' )

#not the correct way to compare numeric values use ==
# if 5 is 5:
#     print ('it is correct')



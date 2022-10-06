class Base():

    #Class Constructor
    def __init__(self): #self similar to this keyword in c++
        print( 'Class Constructor' )
        #self allow defining object to use within the class
        self.place_holder = None
        #without self, the object only exists as a local object
        second_item = None

    #Class Destructor
    def __del__(self):
        print( 'Class Destructor' )

    def __add__(self, RHS):
        #check the type of the RHS and provide solutions for any type
        #type(RHS) == type(int())
        #type(RHS) == type(self)
        print('Add was called')
        print(f'Our RHS is: {RHS}') #python3 allow f in front of the string
        print(f'The type is: {type(RHS)}')

        if type( RHS ) == type( int() ):
            print('We can do something with the integer')
            self.place_holder = 7
    
    #reverse operator overloading
    def __radd__(self, LHS):
        #String formation using .format()
        print( 'The LHS Item is: {0}'.format(LHS) )
    
    def cal_avg(items = None):
        if items is None:
            return
        
    def print_information():
        print('This is the Base Class')

class Derived(Base):
    def __init__(self):
        print('Derived Class Constructor')
        Base.__init__(self)

import Custom_Pkg.Custom_Class as custom

def main():
    base_object = Base()
    base_object2 = Base()
    # RHS Passing Operator Overloading
    base_object + base_object2
    base_object + 7
    # LHS Passing Operation Overloading
    5 + base_object

    derived_object = Derived()

    custom_obj = custom.Clothing_Store('Name', 10, 'Friend', 'Marietta')
    custom_obj.display()

if __name__ == '__main__':
    main()


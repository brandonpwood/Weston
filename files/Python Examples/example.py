# Variable Declaration
x = 10
y = 'this is a string that says its a string'
c = 'c'
b = [] # This is an empty array

full_array = ['3', 4, 3, 'four']

# if/else statements

if 10 < 3:
    print("Wow")
else:
    print("Foo")

if x == 10:
    print("Fantastic")
    x = 1000000
else:
    print("Trash")

# Function Definitions

def some_function(input_1, input_2):
    if(input_1 < input_2):
        print(input_1, "is greater than", input_2)
    else:
        print(input_2, "is greater than", input_1)

def a_function_that_runs_some_function(i1, i2):
    some_function(i1, i2)

def calculate_power(volts, amps):
    return volts*amps


# Loops

for thing in full_array:
    print(thing)
# This does the same thing
for potato in full_array:
    print(potato)

big_number = 0
for x in range(10000000):
    big_number = big_number*x

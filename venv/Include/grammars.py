# integer
number = 49;
pi = 3.141596;
print('the value is:', pi+number);

convert_pi = int(pi);
convet_int = float(number);

print(convert_pi);
print(convet_int);

"""string(comment with # also fine)"""
firstString = 'I know you longer than today'

print(firstString.capitalize());
print(firstString.isalpha());
print(firstString.split(' '));
print(firstString.isdigit());
print('hello'.isalpha());

name = 'Amy Cai';
"""one of the disavantage from python: if I name the variable the same as before and assign new value here, 
original valiable will be modified without any me know(since no error in th edito)"""
number = 110;
place = 'Barneveld';

# two ways to assign arguments in the sentence
print('Hoi, ik ben {0}, leuk om je te ontemueten in {1}, ik hou van the number {2}'.format(name, place, number));
print(f'Nice to meet you {name}, I also live in {place}, I like the number ')

# Boolean or None: difference with other languages, start with T or F for true and false. None is similar to null in other languages.

python_course = True;
javascript_course = False;

print(int(python_course));
print(str(javascript_course));
print(python_course);

other_hunman_planet_found = None;
# transfer_back_to_ancient_country = K; # will give an error that K is not defined
print(other_hunman_planet_found);

# if statement, pyton use intentation instead of {} in if, loop and functions
# if and else both end with :
# all numbers that other than 0 have truthy value.None is treat as false
class_name = 'Big Bug';
if class_name == 'Big':
    print('the class name called big Bug');
else:
    print('the class name is not called big bug');

if other_hunman_planet_found:
    print('there is human being in other planet');
else:
    print('there is no people in other planet');


# if not(check the falthy value)
if class_name != 'Big':
    print('I am checking the falthy value for class name');

# if not is used to check truthy of an value
if not other_hunman_planet_found:
    print('check falthy with the people');

# mutiple if condition: and = && in js, or == || in js

#ternary: it is written in broken English
a = 3;
b = 17;
print('bigger' if a > b else 'smaller'); # smaller


# lists
student_names = ['John', 'Emma', 'Eddie', 'Chris'];
print(student_names[3]); # no -0 things in python, from back, it start with -1
print(student_names[-1]);

print(student_names);

#list function
#add element to the list
student_names.append('Zerk'); # can not add like: student_names[4] = 'Zerk
print(student_names);

#insert()
print('befor insert', student_names);
student_names.insert(2, 'Amy')
print('after insert the name at index 2',student_names);

#if elment in the list
if 'Zerk' in student_names:
    print('Zerk is in the list');
#length of the list
len(student_names);
print('the length of the list is :', len(student_names));

#delete elemnt in the list
del student_names[1];
print(student_names);

# List Slicing
print(student_names[1:]); #won't modify the list itself
print(student_names)

# more function like pop, reverse... can be checked online 'list python3'

#range
range(5, 10, 2); # range has three arguments, start index, end index, and increment

# Loops
for index in range(5, 10, 2):
    print('we are currently at number: {0}'.format(index));

# break and continue: break if fount it, continue will skip the code below but won't stop the loop
print(student_names);
for name in student_names:
    if name == "Chris":
        continue;
    print('Here we have {0}'.format(name));

#while loop

# python Dictionary, it is kind like Json{obj}
# key - value
all_student_name = [{"name": "John", "number": 32, "age": None},
                    {"name": "Eddie", "number": 35, "age": 7},
                    {"name": "Emma", "number": 23, "age": 1},
                    {"name": "Jurrie", "number": 19, "age": 8},
                    ]

print(all_student_name[0]['name']);

#find the value in by ke in case key is not in the object
searchName = all_student_name[1].get('last_name', 'not_defined');
print(searchName);

# get keys or value
print(all_student_name[2].keys());
print(all_student_name[3].values());

# delete
del all_student_name[0]['name'];
print(all_student_name);

del  all_student_name[0];
print(all_student_name);

# Exception, other code use: try...catch and final  normally
try:
    all_student_name[1]['last_name'] = 'Smith';
    second_student_last_name = all_student_name[1]['last_name'];
    order_of_student = 2 + second_student_last_name;

except KeyError as error:
    print('There is error: {0}'.format(error));
except TypeError as error:
    print('There is error: {0}'.format(error));

# handle gernel error:
try:
    all_student_name[5] = 'I can not be added'; # can only use append to add alue for a list
except Exception as error:
    print('Hey, I catchedd an error for you which is: {0}'.format(error));

#other data type:
# byte an bytearray: will continue in python foundamental

#tuple, it is like list but the value can nt be changed

# set and frozenset: unique value only
unsorted_list = [2, 4, 5, 1, 2, 3, 'Monday', 3];
sorted_list = set(unsorted_list);
print(sorted_list);

# Functions
"""user_name = input('Please enter the student name:');
print('user name is', user_name);"""

students = [];

#a variable numbers of arguments like the function print
def var_args(name, *args):
     print(name);
     print(args); # no * infront of args when use it in the funtion

var_args('Jurrie', 17, None, 'Love AWS');

# in order to make the element clear, we use keyword, kwargs
def var_kw_args(name, **kwargs):
    print(name);
    print(kwargs['description'], kwargs['subscribe'], kwargs['tag']);

var_kw_args( "Marks", description = "he like AWS", subscribe = False, tag = "unknow");

# generator, use return can only return first line value, use yiled will return all of the lines until end
def read_students(student_list):
    for lines in student_list:
        yield lines;

# test
my_student_list = ['we love' + "\n", 'nl' +"\n", 'let us try it out' +"\n"];

my_students_container = [];
for student in read_students(my_student_list):
    student = student.rstrip();
    my_students_container.append(student);

print(my_students_container);

# do the comment in the first line within function not outside of the function
def test():
    """this is to tell you that the comment should be within the function now outside"""
    pass

# pypi: where you can find a lot of python package

# flaks: a framework like Djong in python

# pi: like npm for node

# use pip to install pyinstaller, it can be used to creat an excuteble file

#function for repay
def calculate_repay(fixed_amount_per_month, interest_amount, duration):
    base_amount_money = fixed_amount_per_month * 12;
    start_money = base_amount_money;
    total_amount_money = 0;
    for i in range(1, duration+1):
        total_amount_money = start_money*(1+interest_amount);
        start_money = total_amount_money + base_amount_money;
    print('the total amount of money after {2} with interest {1} is: {0}'.format(total_amount_money, interest_amount, duration));

calculate_repay(1000, 00.4, 10);

def testFor(number):
    for index in range(0, number):
        print(index);

testFor(10);






























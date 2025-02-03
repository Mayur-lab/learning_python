#  Day 1 python learn (install process)


                    #                 Steps to Install VS Code Editor and Python Interpreter:
                    # 1. Install VS Code using:
                    # https://code.visualstudio.com

                    # 2. Install "python" extension in VS Code

                    # 3. Install Python Interpreter using:
                    # https://www.python.org/downloads/

                    # 4. Select Python Interpreter in VS Code

                    # All Steps:
                    # https://code.visualstudio.com/docs/py...

                    # Let's see How to Write First Code in Python?






#  Day 2 python learn (keywords & identifiers)

                    # Keywords - reserved words in Python
                    # Identifiers - names given to variables, functions, etc.

                    # Examples:
                    # Keywords: True, False, if, else, elif, class, break, etc.
                    # Identifiers: message, language, number, count, etc.

                    # Rules for Naming an Identifier
                    # Identifiers cannot be a keyword.
                    # Identifiers are case-sensitive.
                    # It can have a sequence of letters and digits. However, it must begin with a letter or _. The first letter of an identifier cannot be a digit.
                    # Whitespaces are not allowed.
                    # We cannot use special symbols like !, @, #, $, and so on.

str = "mayur walunj"
STR = "my name is mayur  i am work in layer one x company "

# True = "my name is mayur  i am work in layer one x company "
# print(True)

# you cannot assing identifier as keyword therefore this is getting error 

print(str)









#  Day 3 python learn ( Variables )


                        # Python Variables
                        # In programming, a variable is a container (storage area) to hold data. For example:

                        # number = 10

                        # Note: Python is a type-inferred language, so you don't have to explicitly define the variable type. It automatically knows that 10 is an integer and declares the number variable as a integer.

                        # Python Constants
                        # A constant is a special type of variable whose value cannot be changed.

                        # Example:
                        # PI = 3.14

                        # Python Literals
                        # Literals are representations of fixed values in a program. They can be numbers, characters, or strings, etc. For example, 'Hello, World!', 12, 23.0, 'C', true, false, etc

                        # ==========



# Day 4 python learn ( data type )
                            #  In computer programming, data types specify the type of data that can be stored inside a variable. For example,

                            # number = 24

                            # Example Code:
                            # num1 = 5
                            # print(num1, 'is of type', type(num1))

                            # num2 = 2.0
                            # print(num2, 'is of type', type(num2))

                            # num3 = 1+2j
                            # print(num3, 'is of type', type(num3))

                            # list = []
                            # tuple = ()
                            # set = {}

                            # ==========
                        # 

#   Day 5 python learn ( input output data ) 

# In this tutorial, we will learn simple ways to display output to users and take input from users in Python with the help of examples.
# In Python, we can simply use the print() function to print output.

# The actual syntax of the print function accepts 5 parameters:
# print(object= separator= end= file= flush=)

# object - value(s) to be printed
# sep (optional) - allows us to separate multiple objects inside print().
# end (optional) - allows us to add specific values like new line "\n", tab "\t"
# file (optional) - where the values are printed. It's default value is sys.stdout (screen)
# flush (optional) - boolean specifying if the output is flushed or buffered. Default: False

# Python Input
# While programming, we might want to take the input from the user. In Python, we can use the input() function.

# num = input("Enter a number: ")



print("LEARNING PYTHON PATH", end= ". ",)
print("mayur walunj learning python")


# num  = input("enter number : ")
# print("enter number :",num)

# numer = int(input("enter number : "))

# print("number :", numer + 10 )

multiplier = int(input("enter Number to Multiplie by 20 : "))


print("result :", multiplier * 20) 



# day 6 python learning ( operations  with  matha functions)

                # Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc. 

                # Example:
                # print (5 + 6)  #11

                # Operator
                # Addition 5 + 2 = 7
                # Subtraction 4 - 2 = 2
                # Multiplication 2 * 3 = 6
                # / Division 4 / 2 = 2
                # % Modulo  5 % 2 = 1
                # ** Power  4 ** 2 = 16


print(20 +30 )

print(50 - 20)

print(10 * 2)

print(10 / 2)

print(10 % 2)

print(2 ** 3)







set1 = ("35kg * 3 more than 5 reps each")
set1sum = 3 * 5

set2 = ("25kg * 3 min 7 reps each ")

set2sum = 3 * 7

set3 = ("15kg * 3 min 10 reps ")

set3sum = 3 * 10

set4 = ("5kg * 3 min 12 reps ")

set4sum = 3 * 12

set5 = ("Bbody weighth  * 3 min 15 reps ")

set5sum = 3 * 15


total_reps = (set1sum + set2sum + set3sum + set4sum + set5sum)


print("Total Reps : ", total_reps)



# if - true, elif - check for other condition if the if condition is not satisfied
# elif

# age = 20
# if age > 18:
#     print("This person is a young adult")
# elif age == 18:
#     print("This person's age is at 18")    
# else:
#     print("The age comparison does not meet conditions")    



# age = input("Enter Your Age")
# attendee_name = input("Enter your name")
# if int(age ) > 18:
#     print(f"{attendee_name} can enter and  receive a drink!")
# elif int(age) >= 16 and int(age) <= 18:
#     print(f"{attendee_name} can enter but receives a juice pack!")
# elif int(age) < 16:
#     print(f"{attendee_name} is too young cannot enter !")


# match statement : used to perform different actions based on different conditions
# day = 6
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("tuesday")        
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5 | 6 | 7:
#         print("Looking forward to the weekend !!!")
#     case _:
#         print("{day} : This day does not exist !!")



# loops - programming statements that will allow you to repeat tasks
# while loop, for loop
# while loop - we can execute a code logic as long as the/a condition is True
# the while loop stops when the condition is False
# incrementors or decrementors ++ : += 1, -- -= 1
# break statement : stop the loop completely when condition met
# / continue statement : skip the condition

# i = 1
# while i < 6:
#     if i == 4:
#         break
#     print(i)
#     i += 1

# # continue
# i = 0
# while i < 6:
#     i += 1
#     if i == 4:
#         continue
#     print(i)    
# else:
#     print(f"{i} : the condition is no longer true")    


# For loop : is used for iteration over sequences
# list, tuple, set, dictionary, string

# x = "banana"     
# for char in x:
#     print(char)

# list_fruits = ["apple", "banana", "Pear"]
# for fruit in list_fruits:
#     x = fruit.upper()    
#     print(x)


# range function range(start, stop, step) step means skip
# FOR LOOP ALSO HAS BREAK , CONTINUE
# for x in range(2,10):
#     if x >= 7:
#         continue
#     print(x)

# nested loops "" for every iteration of the outer loop it must complete the whole iteration of the inner loop
# colors = ["red", "yellow", "green"]
# for x in colors:
#     # for y in list_fruits:
#         print(f"{x} : {y}")    


# password = "" # empty string
# while password != "letmein":
#     password = input("Give me your password:: ")
# print("Access granted !")

# python methods for looping actions
# enumerate() : useful when we want box index and value
# names = ["Bill", "Jane", "Isak"]
# for index,name in enumerate(names):
#     print(index,name)


# # comprehesions : list comprehension : loop one liners
# squares = []        
# for x in range[5]:
#       squares.append(x)
# print(squares)      

# # list comprehension
# squares = [i * i for i in range(5)]
# print(f"squares list comprehension {squares}")

# # traditional loop
# t_squares=[]
# for i in range(5):
#      multiples = i * i
#      t_squares.append(multiples)

# print(f"traditional loop returning a list {t_squares}")

# functions
# reusable block of code designed to perform a specific task
# a function will receive input (arguments or parameters) -> it processes the input in accordance to logic in code block -> gives back a desired output - single ValueError
# define a function in python : def - nameofthefunction():
# process -> absent of process indicate pass (marks a code block as void)
# return -> specifies the return value of a function
# None -> specifies no return was specified for the function
# to be executed functions require to be called : call a function : functionName()

def greet_function():
     greeting = f"Hello, this is the sum of the two numbers given "
     return greeting
# parameters are placeholders for inputs to be processed in a function - max 6 - functions are reusable
def add(a,b):
     result = greet_function()
     sum = a + b
     return f"{result} : {sum}"

print(greet_function())
print(add(20, 10)) # 20, 10 function arguments -> fulfillment for the parameters
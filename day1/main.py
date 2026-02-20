# Print Statement
print("Hello World"); print("hey")


# Use of backslash
x = 1 +     2 \
+3
print(x)

# Indentation
name = "utkarsh"
if name == "Utkarsh":
  print(name)

# Function

def doSum():
    a = 5; b = 6
    sum = a+b;
    return sum

print(doSum())

# Datatypes in Python

a = 10
b=10.5
c=10+10j
d=[1,2,3,4]
e="Hello"
f_tuple=(1,"Hello",4.5,"A")
g_set = {1,"hello",2.33}
h_dict={'a': 2, 'b': "Utkarsh"}
print(type(a)) #int
print(type(b)) #float
print(type(c)) #complex
print(type(d)) #list
print(type(e)) #str
print(type(f_tuple)) #tuple
print(type(g_set)) #set
print(type(h_dict)) #dict


# Console output and handle user data

num1 = input("Please enter first number: ")
num2 = input("Please enter Second number: ")
print("Sum of num1 and num2 is ", int(num1)+int(num2))





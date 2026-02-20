# Math Logical operators

print(3+2)  #5
print(3-2) #1
print(35/5) #7.0
print(37/5) #7.4
print(7*3) # 21
print(10%2) # 0 gives remainder
print(10%3) # 1

num = 12

if num >5 and num < 15:
  print("All true")

num2 = 15
if num2 >5 or num2 < 15:
  print("One true")

print(not(num>10))  #False


# Match statement

http_status = 500

match http_status:
  case 200:
    print("Success")
  case 400:
    print("Not found")
  case 500:
    print("Internal Server error")
  case _:
     print("unknown")      

# Loops
# for loop

fruits = ["Banana" , "Apples" , "Orange" ,"Grapes"]

for i in range(5):
  print(i) # 0 1 2 3 4 on new lines 

for item in fruits:
  print("I love to eat ", item)

# While loop

count=0
while count < len(fruits):
  print("I love ", fruits[count])
  count +=1
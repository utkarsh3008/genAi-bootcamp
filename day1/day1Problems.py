# Return Even Numbers

numbers = [1,2,5,4,6,8,10,11,45]

def getEvenNumbers(numbers):
   for num in numbers:
      if num%2 == 0:
         print(num)
      

getEvenNumbers(numbers)

# Get Sum of all Numbers
def getSum(numbers):
  sum = 0
  for num in numbers:
    sum = sum+num
  return sum

print(getSum(numbers))


# Return the Squared list

def getSquaredList(numbers):
   squared = [x*x for x in numbers]
   return squared

print(getSquaredList(numbers))

# Return a dictionary with Summary

def analyze_user(name , skills):
   summary = {
      "name": name,
      "skills": skills,
      "numberOfSkills": len(skills),
      "isAiEngineer": "AI" in skills
   }
   return summary

print(analyze_user("Utkarsh" , ["React" , "JS", "AI"]))

# Problem on dict

employees = [
   {"name" : "A", "salary":30},
   {"name" : "A", "salary":50},
   {"name" : "A", "salary":45},

]

def getHighestSalary(employees):
   maxSalary = 0
   for emp in employees:
      if maxSalary < emp["salary"]:
         maxSalary = emp["salary"]
   return maxSalary

print(getHighestSalary(employees)) 

def increaseSalary(employees):
   for emp in employees:
      emp["salary"] = emp["salary"] + emp["salary"] * 0.1

   return employees

print(increaseSalary(employees))
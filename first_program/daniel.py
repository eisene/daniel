print("What is your name?")
name = input()
print("How old are you " + name + "?")
age = input()
print("Wow, you're " + age + "!")
print("In a year, you will be " + str(int(age) + 1))
print("In two years, you will be " + str(int(age) + 2))

for year in range(5):
    year = year + 3
    print("In " + str(year) + " years, you will be " + str(int(age) + year))
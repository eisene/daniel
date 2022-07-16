print("What is your name?")
name = input()
print("Hi " + name)

print("How many pennies do you have, " + name + "?")
pennies = int(input())

print("How many nickels do you have, " + name + "?")
nickels = int(input())

print("How many dimes do you have, " + name + "?")
dimes = int(input())

print("How many quarters do you have, " + name + "?")
quarters = int(input())

print("How many dollars do you have, " + name + "?")
dollars = int(input())

total_pennies = pennies + 5*nickels + 10*dimes + 25*quarters + 100*dollars
print("You have " + str(total_pennies) + " pennies")
print("You have " + str(total_pennies/5) + " nickels")
print("You have " + str(total_pennies/10) + " dimes")
print("You have " + str(total_pennies/25) + " quarters")
print("You have " + str(total_pennies/100) + " dollars")

total_dollars = total_pennies/100
if total_dollars > 65:
    print("You can buy a video game!")
if total_dollars > 300:
    print("You can buy a Switch!")
if total_dollars > 20000:
    print("You can buy a car!")
if total_dollars > 450000:
    print("You can buy a house!")
if total_dollars > 10000000:
    print("YOU'RE RICH!!!")
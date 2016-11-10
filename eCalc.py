# eCalc v1.2
# in Python
# by Brendan Gowen
# https://www.github.com/thatoneguy107
# 11/10/2016

from time import sleep as Delay

print("Welcome to eCalc v1.2!\n")

userNum = float(input("What number to you what to multiply? "))
userNum2 = userNum
userExponent = float(input("To what power? "))

i = 1

while i < userExponent:
	userNum = userNum * userNum2
	i = i + 1
	
print("\nThe answer is: " + str(userNum))
print("\nThanks for using eCalc v1.2!")

Delay(2.5)

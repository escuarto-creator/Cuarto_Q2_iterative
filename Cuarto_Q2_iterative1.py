# let the user input an age. Then use the formula s = n(n+1)/2 to calculate the sum of all numbers from 1 to n. and if s==getsum, print verified. Print the result loop.
age = int(input("Enter your age, please :) :"))

while age <= 0:
    print("Invalid! Enter a valid number")
    age = int(input("Enter your age, please :)"))

s = age * (age + 1) / 2

def getsum(age):
    sum = 0
    for i in range(1, age + 1):
        sum += i
    return sum

print(f"The expected sum of all numbers from 1 to {age} is: {s}")
print(f"The actual sum of all numbers from 1 to {age} is: {getsum(age)}")
if s == getsum(age):
    print("Verified!")

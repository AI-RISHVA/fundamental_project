# 1. Print all numbers from 1-100 but skip multiples of 7
for i in range(1,101):
    if i % 7 ==0:
        continue
    print(i)
# 2. Print pattern: * ** *** **** *****
for i in range (1,6):
    print("*" * i)

# 3. Find sum of all odd numbers between 1 and N
n = int(input("enter number:"))
sum = 0
for i in range(1,n+1):
    if i % 2!=0:
        sum += i
        print(f"{n} odd number sum is {sum}")

# 4. Print numbers in reverse from N to 1
n = int(input("enter number:"))
for i in range (n,0):
    print(i)
# 5. Remove spaces from a string
# 6. Print pyramid pattern with numbers
# 7. Find LCM of two numbers
# 8. Print all prime numbers between 1 and N
# 9. Create a guessing game (user has 5 attempts)
# 10. Calculate power of a number without using ** or pow()
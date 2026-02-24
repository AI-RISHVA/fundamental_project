# 1. Print numbers from 1 to 100
for i in range(1,101):
    print(i)

# 2. Print multiplication table of a number
a= int(input("enetr table number:"))
for i in range(1,11):
    print(f"{a} * {i}= {i*a}")

# 3. Calculate sum of first N natural numbers
n= int(input("enetr number:"))
total =0
for i in range(1,n+1):
  total += i
print("sum:",total)

# 4. Print all even numbers between 1 and 50
for i in range(1,51,2):
    print(i)

# 5. Count digits in a number
n= int(input("enter number:"))
count = 0
while n !=0:
   n//=10
   count +=1
print(count)

# 6. Create a simple login system (username/password check)
print("sign in")
a= input("enter username:")
b= input("enter password:")
print("log in")
a1=input("enter username:")
b1= input("enter password:")
if a == a1 and b ==b1:
    print("login successfully!")
else:
    print("please try again!")

# 7. Calculate electricity bill based on units consumed (slabs)
a= int(input("eneter used the units number:"))
if a>1 and a<100:
    print("₹3")
elif a>101 and a<200:
    print("₹5")
elif a>201 and a<300:
    print("₹7")
elif a>300:
    print("₹10")
else:
    print("please enter correct information")

# 8. Check if a triangle is valid given three sides
a= int(input("enetr side a :"))
b= int(input("enetr side b:"))
c= int(input("enetr side c:"))
if a+b>c and b+c>a and c+a>b:
    print("valid triangle")
else:
    print("unvalid triangle")

# 9. Find the largest of 3 numbers using nested if
a= int(input("enetr 1st number:"))
b= int(input("enetr 2nd number:"))
c= int(input("enetr 3rd number:"))
if a>b & a>c:
    print(a,"biggest number")
    if b>c:
        print(b,"biggest number")
else:
    print(c,"biggest number")

# 10. Create a menu-driven program (calculator with choices)
while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice=='5':
        print("Exiting program...")
    break
if choice in ['1','2','3','4']:
    a= float(input("enetr 1st number:"))
    b= float(input("enetr 2nd number:"))
    
    if choice =='1':
        print("sum:",a+b)
    if choice =='2':
        print("sub:",a-b)
    if choice =='3':
        print("mul:",a*b)
    if choice =='4':
        if num2 == 0:
            print("can't divide by 0")
        else:
            print("div:",a/b)    
else:
        print("Invalid choice, try again.")    

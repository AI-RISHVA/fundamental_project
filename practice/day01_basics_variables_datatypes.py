# 1.Write a program to print "Hello, machine learning"
print("Hello, machine learning")

# 2.Take user input for name and age, print formatted output
name = input("ENTER YOY NAME:")
age = int(input("ENTER YOUR AGE:"))
print("name:" ,name)
print("age:",age)

# 3.Convert temperature from Celsius to Fahrenheit (user input)
c = float(input("ENTER CELSIUS NUMBER:"))
f = c*9/5 +32
print(f,"F")

# 4.Create variables of different data types and print their types
integer = 23
float = 89.566666
boolean = True
string ="hello"

print(type(integer))
print(type(float))
print(type(boolean))
print(type(string))


# 5.Write a program to swap two numbers without temp variable
a= int(input("enetr 1st number:"))
b= int(input("enetr 2nd number:"))

a,b = b,a
print(a)
print(b)

# 6. Take multiple inputs in single line and perform arithmetic operations
a, b = map(int, input("Enter numbers: ").split())
print("sum:",a+b)
print("sub:",a-b)
print("mul:",a*b)
print("div:",a/b)


# 7. Create a simple calculator (add, subtract, multiply, divide)
a= float(input("enetr 1st number:"))
b= float(input("enetr 2nd number:"))
op = input("enetr operation:")
if op == "+":
    print("sum:",a+b)
elif op == "-":
    print("sub:",a-b)
elif op == "*":
    print("mul:",a*b)
elif op == "/":
    print("div:",a/b)
else:
    print("please , Enter correct information")

# 8. Check if a number is even/odd using type conversion
a= int(input("enetr number:"))
if a % 2 ==0:
    print("number is  EVEN")
elif a % 2 !=0:
    print("number is ODD")
else:
    print("Enter correct information!")

# 9. Convert seconds to hours:minutes:seconds format
sec_total = int(input("enetr second:"))
hours = sec_total//3600
remaing_sec = sec_total % 3600
min = remaing_sec //60
sec = remaing_sec % 60

print(f"{hours}:{min}:{sec}")

# 10. Create a program that takes user's birth year and calculates age
bday = int(input("enetr birth year:"))
current_year = 2026
birth_year = current_year - bday
print(birth_year)

# 11. Check if a number is positive, negative, or zero
a= float(input("enetr number:"))
if a>0:
    print("POSITIVE")
elif a<0:
    print("NEGATIVE")
else:
    print("ZERO")

# 12. Find maximum of three numbers
a= int(input("enetr 1st number:"))
b= int(input("enetr 2nd number:"))
c= int(input("enetr 3rd number:"))
if a>b & a>c:
    print(a,"biggest number")
elif b>c:
    print(b,"biggest number")
else:
    print(c,"biggest number")

# 13. Check if a year is leap year
year = int(input("enetr year:"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0 ):
    print("LEAP YEAR")
else:
    print("NOT LEAP YEAR")
# 14. Grade calculator (marks to grade conversion)
a= float(input("ENTER MARKS:"))
if a>=90:
    print("GRADE A+")
elif a>=80 and a<90:
    print("GRADE A")
elif a>=70 and a<80:
    print("GRADE B+")
elif a>=60 and a<70:
    print("GRADE B")
elif a>=50 and a<60:
    print("GRADE C")
elif a<50 and a>34:
    print("GRADE D")
else:
    print("FAIL")
# 15. Check if a number is divisible by both 3 and 5
a = int(input("enetr number:"))
if a % 3 == 0 & a % 5 == 0:
    print(a,"is divisible by both 3 and 5.")
else:
    print(a,"is NOT divisible by both 3 and 5.")


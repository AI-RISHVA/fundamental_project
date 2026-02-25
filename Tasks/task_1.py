# Q1 :- Print the given strings as per stated format.
'''Given strings:"Data" "Science" "Mentorship" "Program" "By" "rishva"
Output:Data-Science-Mentorship-Program-started-By-rishva'''
print("Data","Science", "Mentorship" ,"Program",
"By", "rishva",sep="-")

# Q2:- Write a program that will convert celsius value to fahrenheit.
c= int(input("enter your celsius number: "))
f= c*9/5+32
print(f,'f')

# Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
a = int(input("enter number:"))
b = int(input("enter number:"))
a,b =b,a
print(a)
print(b)

# Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.
X1 = int(input("enter number:"))
X2 = int(input("enter number:"))
Y1 = int(input("enter number:"))
Y2 = int(input("enter number:"))

dis= (((X2-X1)**2) +(Y2-Y1)**2)**0.5
print(dis)

# Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
# si=ptr/100
p =int(input("enter amount:"))
t = int(input("enter time:"))
r = int(input("enter rate:"))
si = p*t*r/100
print(si)

#  Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
# For example:Input:heads -> 4,legs -> 12 ;Output:dogs -> 2,chicken -> 2
h = int(input("enter total head:"))
l = int(input("enter total leg:"))
dog=(l - 2*h) // 2
chicken = h-dog
print("number of dogs:-",dog)
print("number of chicken:-",chicken)

# Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
n = int(input("enter the number:"))
sum =0
for i in range(1,n+1):
    sum=sum +i**2

print(sum)

# Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series.Assume all inputs are provided by the user.
a1= int(input("enter 1st term:"))
a2= int(input("enter 2nd term:"))
n= int(input("number of nth term:"))
d=a2-a1
an=a1+(n-1)*d
print(an)

# Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
from fractions import Fraction
a=int(input("Numerator1:"))
b=int(input("Denominator1:"))
c=int(input("Numerator2:"))
d=int(input("Denominator2:"))

f = Fraction(a, b) + Fraction(c, d)  #f= (a*d + b*c)/(b*d)
print(f)

# Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
'''
Input:
Dimensions of the milk tank
H = 20cm, L = 20cm, B = 20cm
Dimensions of the glass 
h = 3cm, r = 1cm
'''
H,L,B=20,20,20 #milk tank
h,r=3,1 #glass
pi = 3.14
number_of_glass = L*B*H/(pi*(r**2)*h)
print("number of glass:",number_of_glass)

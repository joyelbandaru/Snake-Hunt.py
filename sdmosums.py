#VOWELS
'''s=input()
s1=s.lower()
a=s1.count('a')
e=s1.count('e')
i=s1.count('i')
o=s1.count('o')
u=s1.count('u')
print(f"no of vowels:{a+e+i+o+u}")'''


#PALINDROME OR NOT
'''s=input("enter string:")
rev=s[::-1]
if s==rev:
    print("palindrome")
else:
    print("not") '''   

    #LARGEST OF 3 NUMS
'''s=input()
x,y,z=s.split(",")
n1=int(x)
n2=int(y)
n3=int(z)
if n1>n2:
    if n1>n3:
      great = n1
    else:
      great = n2
elif n2>n3:
    if n2>n3:
      great = n2
    else:
      great = n1
elif n3>n1:
    if n3>n2:
      great = n3
    else:
      great = n2   
print(f"greatest num:{n1},{n2},{n3}") '''


#leap
y=int(input())
leap=False
if y%100==0 and y%400 !=0:
    leap=False
elif y%4==0:
    leap=True
else:
    leap=False
print(leap)

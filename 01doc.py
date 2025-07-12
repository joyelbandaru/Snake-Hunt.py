#student grade
'''
sub1=int(input("enter num:"))
sub2=int(input("enter num:"))
sub3=int(input("enter num:"))
total=sub1+sub2+sub3
print(total)
if total>90:
    print("grade a+")
elif 75<=total<=90:
    print("grade a")
elif 50<=total<74:
    print("grade b")  
else:
    print("fail") '''

#age based movie ticket
'''age=int(input("enter age"))
if age<5:
    print("free") 
elif age<=5 & age<18:
    print("INR 100")    
elif age<=19 & age<60:
    print(" INR 200")  
else:
    print("INR 50") '''

'''#number nature checker
n=int(input("enter num:"))
if n>0:
    if n%2==0:
        print("positive and even")
    else:
        print("positive and odd") 
elif n<0:        
    if n%3==0:
        print("negative and div by 3")    
    else:
        print("negative and not div by 3") 
else:
    print("zero") '''

''' # 5  vowel or consonant  
a=input("enter string:")
if a.isalpha():
    if a in 'aeiou':
        print("vowel")
    else:
        print("consonant")
else:
    print("not a num") '''


#electricity bill
a=input("enter number")   
if a<50:
    bill=a*3     
elif a<51 & a<150:
    bill=a*5
else:
    bill =a*8   
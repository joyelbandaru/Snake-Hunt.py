'''n=[10,20,30,40,50]
sum=0
for i in n:
    sum=sum+i
print(sum)'''

'''n=[10,20,30,40,50]
sum=0
length=len(n)
for i in range(0,length):
   sum=sum+ n[i]
print(sum)'''

'''n=[10,20,30,40,50]
sum=0
i=0
length=len(n)
while i<length:
    sum=sum+n[i]
    i+=1
    print(sum)'''

#max and min values in a list
l=[15,2,7,25,10]
max=l[0]
min=l[0]
for i in l:
    if i> max:
        max=i
    if i<min:
        min=i   
print(max,min)         

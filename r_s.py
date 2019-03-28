x= int(input(" Enter number: "))
e = 0
o = 0
 
for i in range(1, x+ 1):
    if(i % 2 == 0):
        e = e + i**3
    else:
        o = o + i**2  #Here odd sum is comig wrong
 
print("The Sum of Even Number",e)
print("The Sum of Odd Number",o) 
print ("total sum is",e+o)
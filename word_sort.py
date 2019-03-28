# I tried by giving the string directly
#y="Hello,I,AM"
#y=y.split(",")
#y=sorted(y)
#print(y)



#give string from user
x=input("input string with comma")
y=[y for y in x.split(",")]
z=sorted(y)
print (z)
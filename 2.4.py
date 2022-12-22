a = {} 
for i in range (0,3,1):
    a[i] = int(input(f"Enter the {i+1}th number "))
a.sort()
print(a)
#print ("Largest number entered is ",a[-1])
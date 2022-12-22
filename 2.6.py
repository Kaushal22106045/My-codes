#let three sides of the triangle be side[]
side = {}
for i in range(0,3,1):
    side[i] = int(input("Enter side length: "))
    if (side[i]<=0):
        print ("Side not possible")
        break 

if (side[i]<=0):
    print ("Sorry triangle's side can't be negative")
elif(side[0]<side[1]+side[2] and side[1]<side[2]+side[0] and side[2]<side[1]+side[0]):
    print ("Yes, traingle is possible")
else:
    print ("No, triangle is not possible")
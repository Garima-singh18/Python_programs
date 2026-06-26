#if,elif,else conditions

Light = str(input("colour of traffic light: "))

if(Light =="red"):
    print("stop")

elif(Light == "yellow"):
    print("wait")

elif(Light == "green"):
    print("Go")

else:
    print("Light is damaged")


marks = int(input("Enter the number: "))

if(marks >= 90):
    print("Passed with grade A ")

elif(marks <= 80 and marks >= 70):
    print("Passed with Grade B")

elif(marks <= 70 and marks >= 50):
    print("Passed with Grade C")

elif(marks <= 50 and marks >= 35):
    print("Passed with Grade D")

else:
    print("fail")
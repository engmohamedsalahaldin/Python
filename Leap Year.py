year = int(input())
if ((year % 4) != 0):
    print("Not a leap year")
elif ((year % 100) != 0):
    print("Leap year")
elif ((year % 400) == 0):
    print("Leap year")
elif ((year % 400) != 0):
    print("Not a leap year")

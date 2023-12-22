Days=[0,'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

while True:
    Number = int(input("Enter a number to print the name of the day: "))

    if Number <= 7:
        print(Days[Number])
    else:
        print('There is no day assigned to that number.')
        break

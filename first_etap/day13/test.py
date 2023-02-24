from random import randint

car_dict = {}
ticket = randint(1, 1000)
print('#' * 30)
print('Computer: Write /help to get help')
help = input('You: ')
while help != '/help':
    print('Computer: Error! Write /help to get help')
    help = input('You: ')
else:
    while True:
        print('#' * 30)
        print('Computer: Write 1 to get ticket')
        print('Computer: Write 2 to check account')
        print('Computer: Write 3 to close ticket')
        number = int(input('You: '))
        while number > 3:
            print('Computer: Error! Write only numbers 1 to 3')
            number = int(input('You: '))
        if number == 1:
            print("Computer: Write your car's number")
            cars_number = input("You: ")
            car_dict["Car's number"] = cars_number.upper()
            print("Computer: Write your car's model")
            cars_model = input("You: ")
            car_dict["Car's model"] = cars_model.upper()
            print("Computer: your ticket's number - ", ticket)
        elif number == 2:
            print("Computer: Write your ticket's number")
            tickets_number = int(input("You: "))
            while tickets_number != ticket:
                print("Computer: Error! Try again")
                tickets_number = int(input("You: "))
            else:
                print(f"Your car {car_dict} in the parking lot")
        elif number == 3:
            print("Computer: Write your ticket's number")
            tickets_number = int(input("You: "))
            while tickets_number != ticket:
                print("Computer: Error! Try again")
                tickets_number = int(input("You: "))
            else:
                print("Computer: Write your /stop close ticket")
                stop = input('You: ')
                while stop != '/stop':
                    print('Computer: Error! Write /help to get help')
                    help = input('You: ')
                else:
                    print('Program stopped')
                    break
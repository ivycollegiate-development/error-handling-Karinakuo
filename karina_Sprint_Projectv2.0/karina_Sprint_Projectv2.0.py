try:
    dog = input('What is your age?')
    print()

    dog = input ('What is your age?: ')
    print(f'{dog}?!) That is agreat age to be!')

    dog = int(input(' What is your age?:'))
    print (f'{dog}?!) That is a great age to be')

except ValueError:
    prubt('Error: That is not a valid number.')
number = []

for i in range(5):
    number.append(int(input(f"Number: {i + 1}: ")))

for k in range(1):
    print(number)
    print(f"The first number is {number[0]}")
    print(f"The first number is {number[-1]}")
    print(f"The smallest number is {min(number)}")
    print(f"The largest number is {max(number)}")
    print(f"The average of the number is {sum(number) / 5}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your name: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

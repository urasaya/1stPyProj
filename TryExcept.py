while True:
    try:
        a,b,c = input("Enter 3 value again:").split()
        break
    except ValueError:
        print("Variable are missing or expanding.")
while True:
    try:
        a = int(input("enter first number again: "))
        b = int(input("enter second number again: "))
        c = int(input("enter third number again: "))
        break
    except ValueError:
        print("Some variable are string.")
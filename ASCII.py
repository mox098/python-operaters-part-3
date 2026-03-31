a = input("Enter a character: ")

if len(a) == 1:
    ascii_value = ord(a)
    print(f"The ASCII value of '{a}' is {ascii_value}")

    if 'A' <= a <= 'Z':
        print("It's an uppercase letter.")
    elif 'a' <= a <= 'z':
        print("It's a lowercase letter.")
    elif '0' <= a <= '9':
        print("It's a digit.")
    else:
        print("It's a special character.")
else:
    print("Please enter just one character.")
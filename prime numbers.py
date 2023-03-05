number = int(input("Enter a number: "))

# Check if the number is greater than 1
if number > 1:
    # Check if the number is divisible by any integer from 2 to the number itself
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


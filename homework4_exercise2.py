try:
    number = int(input("Enter number: "))

# num_in_square started print from 1
    num_in_square = 1
    for i in range(1, number + 1):
        num_in_square = i ** 2
        i += 1
        if number >= num_in_square:
            print(num_in_square, end=" ")

# Error info
except ValueError:
    print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")
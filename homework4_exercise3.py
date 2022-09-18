try:
    number = int(input("Enter number: "))

# prime numbers are greater than 1
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("It's not a prime number")

# operator break used for stop cycle if stateman (num%i==0) satisfied
                break
        else:
            print("It's a prime number")

# if input number is less than or equal to 1, it is not prime
    else:
        print("It's not a prime number")

# Error info
except ValueError:
    print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")
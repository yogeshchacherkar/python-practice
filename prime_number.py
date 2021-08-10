def is_prime(number: int):
    if number in [2, 3]:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, number // 2):
            if number % i == 0:
                return False
        else:
            return True


if __name__ == '__main__':
    while True:
        try:
            number = int(input("\nEnter a positive number: "))

            if number < 2:
                print("INVALID INPUT! Please enter value greater than 1.")
                continue

            elif is_prime(number):
                print("%d is a prime number." % number)

            else:
                print("%d is NOT a prime number." % number)

            if not input("\nDo you want to continue? (Y/n):  ").lower() in ['y', 'yes']:
                print("\nGood Bye!")
                break

        except ValueError:
            print("Please enter valid input!")

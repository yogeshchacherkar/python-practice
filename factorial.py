def factorial(number: int):
    if number in [1, 2]:
        return number

    else:
        fact = 1

        for i in range(2, number + 1):
            fact *= i

        return fact


if __name__ == '__main__':
    while True:
        try:
            number = int(input("\nEnter a positive number: "))

            if number < 1:
                print("INVALID INPUT! Please enter value greater than 0.")
                continue

            else:
                print("%d! = %d" % (number, factorial(number)))

            if not input("\nDo you want to continue? (Y/n):  ").lower() in ['y', 'yes']:
                print("\nGood Bye!")
                break

        except ValueError:
            print("Please enter valid input!")

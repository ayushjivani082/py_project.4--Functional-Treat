# functional treat

print("Welcome to the Data Analyzer and Transformer Program")

total_elements = 0
overall_mean = 0
arr = []


def calculate_average(data):
    """calculate average of the data."""
    return sum(data) / len(data)


def find_unique(data):
    """find unique values from the data."""
    return list(set(data))


def update_summary(data):
    """update global dataset summary."""
    global total_elements, overall_mean
    total_elements = len(data)
    overall_mean = sum(data) / len(data)


def display_args(*values):
    """display multiple values using args."""
    print("Values using *args:", values)


def display_kwargs(**details):
    """display details using kwargs."""
    for key, value in details.items():
        print(key, ":", value)


def get_statistics(data):
    """return multiple statistics of the dataset."""
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = sum(data) / len(data)
    return minimum, maximum, total, average


def factorial(fact):
    """calculate factorial using recursion."""
    if fact == 0 or fact == 1:
        return 1
    else:
        return fact * factorial(fact - 1)


def fibonacci(n):
    """calculate Fibonacci using recursion."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def display_2d(data):
    """display 2D list in grid format."""
    print("\n2D Data:")
    for row in data:
        print(*row)


def flatten_data(data):
    """convert 2D list into 1D list."""
    if len(data) > 0 and isinstance(data[0], list):
        result = []
        for row in data:
            result.extend(row)
        return result
    else:
        return data


while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial and Fibonacci (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("Enter your choice [1 to 7]: "))

    if choice == 1:

        print("\nChoose data type:")
        print("1. 1D List")
        print("2. 2D List")

        data_choice = int(input("Enter your choice: "))

        if data_choice == 1:

            array_input = input(
                "Enter data for a 1D array (seperated by spaces):\n"
            )

            arr = list(map(int, array_input.split()))

            update_summary(arr)

            print("Data has been stored successfully!!")
            print("")

        elif data_choice == 2:

            rows = int(input("Enter number of rows: "))
            arr = []

            for i in range(rows):
                row = list(
                    map(int, input("Enter row values separated by spaces: ").split())
                )
                arr.append(row)

            print("2D Data has been stored successfully!!")
            display_2d(arr)

            print("")

        else:
            print("Invalid choice!")
            print("")


    elif choice == 2:

        data = flatten_data(arr)

        print("\nData Summary:")
        print("- Total element :", len(data))
        print("- Minimum value :", min(data))
        print("- Maximum value :", max(data))
        print("- Sum of all value :", sum(data))
        print("- Average value :", calculate_average(data))

        display_kwargs(
            total_elements=len(data),
            minimum=min(data),
            maximum=max(data),
            total=sum(data),
            average=calculate_average(data)
        )

        print("\nUnique values :", find_unique(data))

        print("")


    elif choice == 3:

        fact = int(input("Enter a number to Calculate its factorial: "))

        print("Factorial of", fact, "is :", factorial(fact))

        fib = int(input("Enter position for Fibonacci: "))

        print("Fibonacci value at position", fib, "is :", fibonacci(fib))

        print("\nFunction Documentation:")
        print(factorial.__doc__)
        print(fibonacci.__doc__)

        print("")


    elif choice == 4:

        data = flatten_data(arr)

        num = int(
            input(
                "\nEnter a threshold value to filter out data below this value:\n"
            )
        )

        filtered_data = list(filter(lambda x: x >= num, data))

        print(f"Filtered Data (values >= {num}):")
        print(*filtered_data, sep=", ")

        doubled_data = list(map(lambda x: x * 2, data))

        print("Data after applying lambda with map:")
        print(*doubled_data, sep=", ")

        print("")


    elif choice == 5:

        data = flatten_data(arr)

        print("Choose sorting option:")
        print("1. Ascending")
        print("2. Descending")

        num = int(input("Enter your choice: "))

        if num == 1:

            data.sort()

            print("Sorted data in Ascending order :", data)
            print("")

        elif num == 2:

            data.sort(reverse=True)

            print("Sorted data in Descending order :", data)
            print("")

        else:

            print("Invalid choice! Please Enter right choice [1 - 2]!!!")
            print("")

        two_d_data = [[3, 20], [1, 40], [2, 10]]

        sorted_rows = sorted(two_d_data, key=lambda x: x[1])

        print("2D List sorted using sorted():")
        for row in sorted_rows:
            print(row)

        print("")


    elif choice == 6:

        data = flatten_data(arr)

        print("Dataset Statistics:")

        minimum, maximum, total, average = get_statistics(data)

        print("- Minimum value :", minimum)
        print("- Maximum value :", maximum)
        print("- Sum of all value :", total)
        print("- Average value :", average)

        display_args(minimum, maximum, total, average)

        print("\nGlobal Summary:")
        print("- Total elements :", total_elements)
        print("- Overall mean :", overall_mean)

        print("")


    elif choice == 7:

        print(
            "\nThank you for using the Data Analyzer and Transformer Program. Goodbye!!"
        )
        print("")

        break

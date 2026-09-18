# Functional Treat

print("Welcome to the Data Analyzer and Transformer Program")
total_elements = 0
overall_mean = 0
arr = []

def calculate_average(data):
    return sum(data) / len(data)

def find_unique(data):
    return list(set(data))

def update_summary(data):
    global total_elements, overall_mean
    total_elements = len(data)
    overall_mean = sum(data) / len(data)

def display_args(*values):
    print("Values using *args:", values)

def display_kwargs(**details):
    for key, value in details.items():
        print(key, ":", value)

def get_statistics(data):
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = sum(data) / len(data)
    return minimum, maximum, total, average

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def display_2d(data):
    print("\n2D Data:")
    for row in data:
        print(*row)

def flatten_data(data):
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
    print("2. Display Data Summary")
    print("3. Calculate Factorial and Fibonacci")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")
    choice = int(input("Enter your choice [1 to 7]: "))

    if choice == 1:
        print("\nChoose data type:")
        print("1. 1D List")
        print("2. 2D List")
        data_choice = int(input("Enter your choice: "))

        if data_choice == 1:
            values = input("Enter data separated by spaces:\n")
            arr = list(map(int, values.split()))
            update_summary(arr)
            print("Data has been stored successfully!")

        elif data_choice == 2:
            rows = int(input("Enter number of rows: "))
            arr = []
            for i in range(rows):
                row = list(map(int, input("Enter row values separated by spaces: ").split()))
                arr.append(row)
            data = flatten_data(arr)
            update_summary(data)
            print("2D Data has been stored successfully!")
            display_2d(arr)

        else:
            print("Invalid choice!")

    elif choice == 2:
        data = flatten_data(arr)
        print("\nData Summary:")
        print("- Total elements :", len(data))
        print("- Minimum value :", min(data))
        print("- Maximum value :", max(data))
        print("- Sum of all values :", sum(data))
        print("- Average value :", calculate_average(data))
        print("\nDetails using **kwargs:")
        display_kwargs(
            total_elements=len(data),
            minimum=min(data),
            maximum=max(data),
            total=sum(data),
            average=calculate_average(data)
        )
        print("\nUnique values :", find_unique(data))

    elif choice == 3:
        number = int(input("Enter a number to calculate factorial: "))
        print("Factorial of", number, "is :", factorial(number))
        position = int(input("Enter position for Fibonacci: "))
        print("Fibonacci value at position", position, "is :", fibonacci(position))

    elif choice == 4:
        data = flatten_data(arr)
        number = int(input("\nEnter threshold value: "))
        filtered_data = list(filter(lambda x: x >= number, data))
        print("Filtered Data:", filtered_data)
        doubled_data = list(map(lambda x: x * 2, data))
        print("Data after using map and lambda:", doubled_data)

    elif choice == 5:
        data = flatten_data(arr)
        print("\nChoose sorting option:")
        print("1. Ascending")
        print("2. Descending")
        sort_choice = int(input("Enter your choice: "))

        if sort_choice == 1:
            data.sort()
            print("Sorted data in Ascending order:", data)

        elif sort_choice == 2:
            data.sort(reverse=True)
            print("Sorted data in Descending order:", data)

        else:
            print("Invalid choice!")

        two_d_data = [
            [3, 20],
            [1, 40],
            [2, 10]
        ]
        sorted_rows = sorted(two_d_data, key=lambda x: x[1])
        print("\n2D List sorted using sorted():")

        for row in sorted_rows:
            print(row)

    elif choice == 6:
        data = flatten_data(arr)
        minimum, maximum, total, average = get_statistics(data)
        print("\nDataset Statistics:")
        print("- Minimum value :", minimum)
        print("- Maximum value :", maximum)
        print("- Sum of all values :", total)
        print("- Average value :", average)
        display_args(minimum, maximum, total, average)
        print("\nGlobal Summary:")
        print("- Total elements :", total_elements)
        print("- Overall mean :", overall_mean)

    elif choice == 7:
        print("\nThank you for using the Data Analyzer and Transformer Program.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

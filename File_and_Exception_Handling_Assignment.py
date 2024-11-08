# File and Exception Handling Assignment

# Exercise 1: Write a Python program to read a file and display its contents.
filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    print(file.read())


# Exercise 2: Write a Python program to copy the contents of one file to another file.
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
with open(source_file, 'r') as src:
    with open(destination_file, 'w') as dst:
        dst.write(src.read())
print("File copied successfully.")


# Exercise 3: Write a Python program to read the content of a file and count the total number of words
# in that file.
filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    words = file.read().split()
    print("Total number of words:", len(words))


# Exercise 4: Write a Python program that prompts the user to input a string and converts it to an integer.
# Use try-except blocks to handle any exceptions that might occur.
user_input = input("Enter a number: ")
try:
    number = int(user_input)
    print("The number is:", number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")


# Exercise 5: Write a Python program that prompts the user to input a list of integers and raises an exception
# if any of the integers in the list are negative.
try:
    numbers = list(map(int, input("Enter a list of integers: ").split()))
    for num in numbers:
        if num < 0:
            raise ValueError("Negative numbers are not allowed.")
    print("The list of integers is:", numbers)
except ValueError as e:
    print("Error:", e)


# Exercise 6: Write a Python program that prompts the user to input a list of integers and computes the
# average of those integers. Use try-except blocks to handle any exceptions that might occur.use the finally clause
# to print a message indicating that the program has finished running.
try:
    numbers = list(map(int, input("Enter a list of integers: ").split()))
    average = sum(numbers) / len(numbers)
    print("The average is:", average)
except ValueError:
    print("Error: Please enter valid integers.")
finally:
    print("Program has finished running.")


# Exercise 7 : Write a Python program that prompts the user to input a filename and writes a string to that
# file. Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no
# exception occurred.
try:
    filename = input("Enter the filename: ")
    string = input("Enter the text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(string)
    print("Welcome! The string has been successfully written.")
except Exception:
    print("Error: Could not write to the file.")
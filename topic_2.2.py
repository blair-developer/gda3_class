# Example: Conditions
age = 12  # Assigns the value 12 to the variable 'age'

if age < 18:  # Checks if 'age' is less than 18
    print("You are a minor.")  # If true, prints "You are a minor."
elif age == 18:  # Checks if 'age' is exactly 18
    print("You are 18 years old.")  # If true, prints "You are 18 years old."
else:  # If none of the above conditions are true
    print("You are an adult.")  # Prints "You are an adult."

# Example: For Loop
numbers = [1, 2, 3, 4, 5]  # Creates a list of numbers

for number in numbers:  # Loops through each number in the list 'numbers'
    print(number)  # Prints the current 'number' in the loop

# Example: While Loop
count = 0  # Initializes the variable 'count' to 0

while count < 5:  # Loops as long as 'count' is less than 5
    print(count)  # Prints the current value of 'count'
    count += 1  # Increments 'count' by 1

# Example: Lists
fruits = ["apple", "banana", "cherry"]  # Creates a list called 'fruits' with three items
print(fruits)  # Prints the entire 'fruits' list

# Example: Tuples
coordinates = (10.0, 20.0)  # Creates a tuple called 'coordinates' with two floating-point numbers
print(coordinates)  # Prints the entire 'coordinates' tuple

# Example: Dictionaries
student = {"name": "John", "age": 22, "courses": ["Math", "CompSci"]}  # Creates a dictionary called 'student' with keys 'name', 'age', and 'courses'
print(student)  # Prints the entire 'student' dictionary

# Example: Sets
unique_numbers = {1, 2, 3, 2, 1}  # Creates a set called 'unique_numbers' with unique elements 1, 2, and 3
print(unique_numbers)  # Prints the entire 'unique_numbers' set (duplicates are removed)

# Example: Functions
def greet(name):  # Defines a function called 'greet' that takes one parameter 'name'
    return f"Hello, {name}!"  # Returns a formatted string with the name

print(greet("Alice"))  # Calls the 'greet' function with the argument "Alice" and prints the result
print(greet("Bob"))  # Calls the 'greet' function with the argument "Bob" and prints the result

# Example: Combining Conditions, Loops, Data Structures, and Functions

def analyze_scores(scores):  # Defines a function called 'analyze_scores' that takes one parameter 'scores' (a list of scores)
    average = sum(scores) / len(scores)  # Calculates the average of the scores
    print(f"Average Score: {average}")  # Prints the average score

    if average >= 90:  # Checks if the average score is 90 or above
        grade = 'A'  # If true, assigns 'A' to the variable 'grade'
    elif average >= 80:  # Checks if the average score is 80 or above
        grade = 'B'  # If true, assigns 'B' to the variable 'grade'
    elif average >= 70:  # Checks if the average score is 70 or above
        grade = 'C'  # If true, assigns 'C' to the variable 'grade'
    elif average >= 60:  # Checks if the average score is 60 or above
        grade = 'D'  # If true, assigns 'D' to the variable 'grade'
    else:  # If none of the above conditions are true
        grade = 'F'  # Assigns 'F' to the variable 'grade'
    
    print(f"Grade: {grade}")  # Prints the final grade

# List of scores
student_scores = [85, 90, 78, 92, 88]  # Creates a list of scores called 'student_scores'

# Call the function
analyze_scores(student_scores)  # Calls the 'analyze_scores' function with 'student_scores' as the argument

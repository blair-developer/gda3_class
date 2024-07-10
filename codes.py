# Example: Conditions
age = 12

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are 18 years old.")
else:
    print("You are an adult.")


# Example: For Loop
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# Example: While Loop
count = 0

while count < 5:
    print(count)
    count += 1

DATA STRUCTURES
# Example: Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Example: Tuples
coordinates = (10.0, 20.0)
print(coordinates)

# Example: Dictionaries
student = {"name": "John", "age": 22, "courses": ["Math", "CompSci"]}
print(student)

# Example: Sets
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)


# Example: Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))


# Example: Combining Conditions, Loops, Data Structures, and Functions

def analyze_scores(scores):
    average = sum(scores) / len(scores)
    print(f"Average Score: {average}")

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"Grade: {grade}")

# List of scores
student_scores = [85, 90, 78, 92, 88]

# Call the function
analyze_scores(student_scores)
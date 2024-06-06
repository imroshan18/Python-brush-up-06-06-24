#basics 
print("hello world")
print("name")

#variables
age = 20
price = 19.95
first_name = "Roshan"
is_online = False
print(age)


#input
name = input("What is your name?")
print("Hello"+ name)

#data types
int()
float()
bool()
str()


# Create a list
fruits = ["apple", "banana", "cherry"]

# Append
fruits.append("orange")

# Insert
fruits.insert(1, "blueberry")

# Remove
fruits.remove("banana")

# Sort
fruits.sort()

print(fruits)


# Create a tuple
my_tuple = (1, 2, 3)

# Access elements
print(my_tuple[1])

# Tuples are immutable, so we can't change them directly

# Create a dictionary
my_dict = {"name": "Alice", "age": 25}

# Access elements
print(my_dict["name"])

# Add elements
my_dict["city"] = "New York"

print(my_dict)


# Create a set
my_set = {1, 2, 3, 4, 5}

# Add elements
my_set.add(6)

# Remove elements
my_set.remove(3)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a | set_b
intersection = set_a & set_b
difference = set_a - set_b

print(union)
print(intersection)
print(difference)

#Conditinal statements
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

 # Simple lambda function
add = lambda x, y: x + y
print(add(2, 3))

# Lambda with map function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Enumerate over a list
colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(index, color)

# Zip two lists
names = ["Roshan", "Bobby", "Deepak"]
ages = [25, 30, 35]
combined = zip(names, ages)

for name, age in combined:
    print(f"{name} is {age} years old.")

import random

# Generate a random number
rand_num = random.randint(1, 100)
print(rand_num)

# Random choice from a list
colors = ["red", "blue", "green", "yellow"]
random_color = random.choice(colors)
print(random_color)


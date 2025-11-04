# connor 
# notes2

## example 1
weather = input("whats the weather like?")

if weather == "rainy":
    ...
else:
    print("I see...")

# string methods example 
if weather.lower() == "rainy":
    ...

### useful methods 
x = ("absolutelynothingijshaveocdanditsannoyingtoseeredlines")

x.strip()
x.strip("a")
x.split(" ")
x.upper()
x.lower()
x.title()

## example 2 

#ask the user for their name 
name = input("whats ur name") 

# remove white spaces
name = name.strip()

# print the output
print(f"hello, {name}")

# ask the user for their name
name = input("whats ur name ")

# remove whitespace from the string 
# capitalize the first letter of each
name = name.strip().title()

# print the output
print(f"hello, {name}")

# ask the user for their name 
# remove white spaces
# capitalize the first letter of each word
name = input("whats ur name").strip.title

# print the output
print(f"hello, {name}")
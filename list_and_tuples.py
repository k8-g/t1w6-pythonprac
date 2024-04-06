
# Non-primitive data types - hold/store multiple pieces of data

# List - Array - collection of data - indexed - mutable (changed)
numbers = [ 13, 2, 5, 98, 56 ]
#           0   1  2   3   4
print(numbers)
print(numbers[2])

numbers[2] = 10
print(numbers)

# adds to the end of list
numbers.append(42)
print(numbers)

# inserts into list where instructed
numbers.insert(2, 16)
print(numbers)

# removes the end number from list
numbers.pop()
print(numbers)

# removes chosen number from list
numbers.remove(98)
print(numbers)

# sort into acsending order
numbers.sort()
print(numbers)

# sorts descending order
numbers.reverse()
print(numbers)

# prints how many numbers there are
print(len(numbers))

# index, count

print("\n\n\n\n")


# Tuple - collection of data - indexed - immutable (cannot be changed)

# () - small brackets - parentheses
# {} - curly brackets - curly brackets
# [] - big brackets - square brackets

names = ( "John", "Jane", "Mike", "Jane", "Jane" )
#           0       1       2       3       4

print(names)
print(names[1])
# names[2] = "Steve" - this one does not work in a tuple
# names.append("Steve") - Does not work
# print(len(names)) - works in a tuple
print(names.count("Jane"))


days_of_the_week = ( "Monday", "Tuesday", "Wednesday", "...." )
co_ordinates_of_some_famous_place = ( 123.56, 20.2 )
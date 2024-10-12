'''

## Lab exercise 2

Using comprehension,create a new list of tuples from two given lists:

### sample calls

list1[1,2,3]
list2["mark","alice","john]

result: listOfTuple[(1,"mark"),(2,"alice"),(3,"john")]

'''

# Create class
class list_of_tuple_generator:
    def __init__(self, numbers, names):
        self.numbers = numbers
        self.names = names

# Generate tuples
# Lists
# Generate and print the list of tuples
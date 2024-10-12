
''' 

from a given list of integers, create a new list using comprehension that will compute the square of odd integer elements.

sample calls

[2,4,3] == [9]
[0,0,1,1] == [1,1] 

'''

# Create class
class odd_sqaure_calculator:
    def __init__(self, elements) -> None:
        self.elements = elements

# Search for the odd elements in the list/s and square them
    def square_odd_numbers(self):
        return [x**2 for x in self.elements if x % 2 != 0]

# Display the result


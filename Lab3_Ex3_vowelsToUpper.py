'''
    ### Provide a list comprehension that implementation for a function called vowelsToUpper with the following signature:

    method name : vowelsToUpper

    input argument : String 

    return argument : String

    vowelsToUpper must return a version of its String argument with all its vowels changed to their uppercase forms. Nonvowel characters stay as is.

    ### Sample Calls

    vowelsToUpper "" == ""

    vowelsToUpper "Hello, world!" == "HEllO, wOrld!"

    vowelsToUpper "hello hi bye" == "hEllO hI byE"

'''


# Create class
class vowel_converter:
    def __init__(self):
        pass
# Convert vowels to uppercase
    def vowels_to_upper(self, input_string):
        return ''.join([char.upper() if char in 'aeiou' else char for char in input_string])
# Input strings
# Print results
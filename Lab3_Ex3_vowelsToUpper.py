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
    def vowelsToUpper(self, input_string):
        return ''.join([char.upper() if char in 'aeiou' else char for char in input_string])
    
convert_vowels = vowel_converter()

# Input strings
phrase1 = "Railey Guinto"
phrase2 = "Antipolo City"

# Print results
print(f'"{phrase1}" {"==" :>5} "{convert_vowels.vowelsToUpper(phrase1)}"')
print(f'"{phrase2}" {"==" :>5} "{convert_vowels.vowelsToUpper(phrase2)}"')
# This is a code snippet that cover majorly on Python strings

# Python string is a collection of letters, words, or other characters is called a string.
# It is one of the basic data structures that serve as the foundation for manipulating data.
# The 'str' class is a built-in string class in Python.
# Because Python strings are "immutable," they cannot be modified after they have been formed.
# Python strings are always surrounded by single quotes('') or double quotes(""):
# "Python" is same as 'Python'
# Python Strings are displayed using the 'print()' function

print('Hello team, this is a Python String')

# Python strings can also be assigned to a variable then accessed later in the program
name = 'Moses Nielsen'
print('Hello', name)

# how to get input from user in string format
# using the 'input' function to get user input will by default give you a string value
country = input('Enter your country of residence: ')
print('Country:', country)

# formatted strings help us to simply python code by combining assigned value and string
# using 'f' and {} curly brackets helps navigate this

print(f'Hey {name}')

# Multiline strings
# You can assign a multiline string to a variable by using three quotes:
email = '''
Dear Team,
This is to notify you that the deadline of project submission has been pushed to Monday

Regards,
Moses Nielsen.
'''
print(email)
# accessing individual letters in  strings
# a string is an array, which means individual elements can be accessed
# you can find and display the letter in a specific position in a string like 'Python'
word = 'Python'
first_letter = word[0]
print(first_letter)  # this will print 'P' in the terminal

# Looping through a string
# being an array, string can be looped through using 'for loop'
loop = country
for letter in loop:
    print(letter)

# converting strings into upper, lower or sentence cases
uppercase = country.upper()  # converts to UPPERCASE
lowercase = country.lower()  # converts to lowercase
sentence_case = country.capitalize()  # converts to Sentence case
print(f'''UPPERCASE: {uppercase}
lowercase: {lowercase}
Sentence Case: {sentence_case}
''')

# let's check if we have the right results by using true or false function in python

upper = uppercase.isupper()
lower = lowercase.islower()
print(f'''
Is our Code in UPPERCASE? - {upper}
Is our Code in lowercase? - {lower}
''')
# length of a string
# if you want to the length of a string use the 'len()' function
print(len(name))  # remember our variable name is 'Moses Nielsen' and has 13 bits including the space

# checking string
# to check if a certain character or phrase is in a string we use 'in' function
name_check = 'Alukwe' in name  # this is to check whether the phrase 'Alukwe' is in the name Variable 'Moses Nielsen'
print(name_check)
if 'Alukwe' in name:
    print('Yee, we found a bug!!!')

if 'Alukwe' not in name:
    print('Yee, no bugs found!')

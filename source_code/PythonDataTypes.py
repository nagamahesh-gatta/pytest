# Textual data represented in python called Strings
print('Hello World!')

# unlike other programming language end of statement no required semicolons
# use either single or double quotes to define value
# variable name should not start with number

''' 
    Documentation quotation or Multiline comments
'''

message = "Hello World!..."
print(message)
print("Length of the message is: ", len(message))

# We use an index to access characters in a string.
print(message[0], message[6])

# slicing [start_position : up_to : step_size]
print(message[0: 5])
print(message[:5]) # start from the beginning u
print(message[6:])  # If the "up_to" part is not mentioned, it implies that the index is used to access characters in
                    # the string up to and including the last character.

# Methods

print("Display message in lower case: ", message.lower())
print("Display message in upper case: ", message.upper())
print("Display message in capitalize method", message.capitalize())

statement = "If the up_to part is not mentioned, it implies that the index is used to access characters in \
            the string up to and including the last character"

print("Number of times", statement.count('is'))

print("Find is method return character index. If it's return -1 if the search item was not found: ", message.find("World"))

print("Replace method takes two argument first takes what argument need to replace, next argument takes new message to /"
      "to replace: ", message.replace("World", "Universe"))

greetings = 'Hello'
name = "Naga Mahesh Gatta"

print(f'{greetings} {name.capitalize()}. Welcome')
print("Display all methods: ", dir(message))
print(help(str))
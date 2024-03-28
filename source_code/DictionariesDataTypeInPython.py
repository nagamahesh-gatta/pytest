# Dictionary
# Dictionaries are immutable data type
# dictionaries working similar like as real world dictionary. searching value by using key
# if searching for key if it's not available in dictionary you will get error. Instead of doing that /
# use get method if the key is not available it returns None


student = {'name':'John', 'age':25, 'courses':['Math', 'Compsci']}
student.update({'name':'Jane','age':25, 'courses':['Math', 'Compsci']})
print(student.get('Phone'))
print(student.get('Phone', 'Not Found'))
student['Phone'] = '55555-55555'
student['name'] = 'jane'
print(student)

# TO delete a value from dictionary
age = student.pop('age')
#del student['age']

print(student.keys())
for key in student.keys():
    print(key)

print(student.values())

for value in student.values():
    print(value)

print(student.items())
for key, value in student.items():
    print(f'{key} : {value}')




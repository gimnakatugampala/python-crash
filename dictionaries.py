# Dictionaries

# Create Dict
person = {
    'first_name':'Gimna',
    'last_name':'Katugampala',
    'age':21
}

# Use Constructor
# person2 = dict(first_name='Gimna',last_name='Katugampala')

# print(person2 ,type(person2))

# # get value
# print(person['first_name'])
# print(person.get('last_name'))

# Add key/value
person['phone'] = '55-5555'

# Get dist keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# get length
print(len(person2))

print(person)

# List Dict
people = [
    {'name':'Jeff','age':20},
    {'name':'Smith','age':23}
]

print(people[1]['name'])
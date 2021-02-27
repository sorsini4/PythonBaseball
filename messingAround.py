print('USING SPLIT ON A STRING')

string = 'this is our string'

print('The string we use is \'this is our string\'')
string = string.split(' ')

print('This is using split on the s ')
print(string)

print('USING JOIN ON AN ARR OF STRINGS')

str2 = ['this', 'is', 'our', 'string']
print('This is using join on the arr version of the string\' ' + ' '.join(str2) + '\'')

print('FORMATTED STRINGS USING STRING.FORMAT')

first_name = 'Steve'
last_name = 'Orsini'
age = 23
amount_of_pets = 1
dog = 'Maverick'

my_string = f'{last_name}, {first_name}, is {age} years old. He has a dog named {dog}, and thats his {amount_of_pets} pet(s).'

print(my_string)


print('DICTONARIES')

player = {
    'name': 'Mike Trout',
    'hits': 120
}

#the get method takes two arguments, the first being what you want to access from the dictonary, and the second
#being what value you want to return if the key is not found within the dictonary (as seen with the at_bats
#it will return a zero

hits = player.get('hits', 0)
at_bats = player.get('at_bats', 0)

print('Hits:', hits)
print('At bats:', at_bats) 

#way of checking if a key exists or not
value = player['hits']
print(value)

if 'name' in player:
    print(player['name'])

#iterating over the dictonary
for k, v in player.items():
    print(f'{k}: {v}') 

teams = {
    'St. Louis': 'Cardinals',
    'Cincinatti': 'Reds',
    'Pittsburgh': 'Pirates',
    'Chicago': 'Cubs',
    'Milwuakee': 'Brewers'
}

for k, v in teams.items():
    print(f'The {v} belong to the city of {k}')

our_list = []

for i in range(0, 100, 5):
    our_list.append(i)

print(our_list)

#much simpler way to do the above code (lines 70-73)
the_list = [i for i in range(0, 100, 5)]
print(the_list)

#in python, there is no ++ or -- operators, there is though the += -= *= /= operators, which allow for ++ in the form of var+=1
i = 0
while i < 6:
    print(i)
    i+=1


"""
Print each persons name and twitter handle, using groups, should look like:

==============
Full Name / Twitter
==============

Derek Hawkins / @derekhawkins
Norrbotten Governor / @sverik
Ryan Butz / @ryanbutz

etc.
"""
import re

# Open the file
file = open('./names.txt', encoding='utf-8')
data = file.read()
file.close()

# Gather each line of the input specifically
lines = re.findall('.*', data)

# Print heading
print('\n' + '='*28 + '\n Fullname / Twitter Handle \n' + '='*28 + '\n')

# Print full names and twitter handles for lines that have both
for line in lines:
    name_list = re.findall('[\w]+,[\s][\w]+', line)
    name = ""
    if name_list:
        comma_index = name_list[0].find(',')
        name = name_list[0][comma_index + 1:] + " " + name_list[0][:comma_index]
    twitter = re.findall('[\s]@[\w\d]+', line)
    if twitter and name:
        print(f'{name} / {twitter[0]}')

print('\n')

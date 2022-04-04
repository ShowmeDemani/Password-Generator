import random

Capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrstuvwxyz'
nums = '1234567890'
special_characters = '[]?!@#%'

length = 9

all = Capital + lower_case + nums + special_characters
password = ''.join(random.sample(all, length))

print("You're new random generated password: " + password)








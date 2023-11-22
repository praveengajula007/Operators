user = {
    "name": "Praveen",
    "gender": "male",
    "occupation": "Agriculture"
    }

#if 'age' in user:
 #   print('Age is present in the dictionary')
#else:
#    print('Age is not present in the dictionary')

for key, value in user.items():
    print(key, value)
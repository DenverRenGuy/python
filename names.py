def print_list(list):
    for item in list:
        print '%s %s' % (item.values()[0], item.values()[1])

def print_dict(dict):
    count = 0
    for key, data in dict.items():
        print key
        count = 1
        for value in data:
            print '%d - %s %s - %d ' % (count, value.values()[0], value.values()[1], len(value.values()[0])+len(value.values()[1]))



#Function Test
#Part 1
students = [
     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#print_list(students)

#Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print_dict(users)

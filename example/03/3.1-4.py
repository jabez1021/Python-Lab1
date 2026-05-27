user = {'name' : 'alghost', 'email' : '.....@gmail.com', 'age' : 19}

if user.has_key('email'):
    if '@' not in user['email']:
        print('Wrong email')
    else:
        print('Email: ' + user['email'])
else:
    print('No email')

student = []
if user.has_key('age'):
    if user['age'] < 20:
        if user['name'] not in student:
            print('Name: ' + user['name'])
            student.append(user['name'])
    else:
        print('Not student')
else:
    print('No age')

if not student:
    print('No students')
else:
    print(student)

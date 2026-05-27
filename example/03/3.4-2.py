emails = ['abc@gmail.com', 'efg@gmail.com', 'wrongemail', 'ghf@gmail.com']

for email in emails:
    if '@' not in email:
        continue
    print(email)

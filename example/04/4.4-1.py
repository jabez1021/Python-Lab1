class Email:
    sender = ""

    def send_mail(self, recv, subject, contents):
        print("From:\t" + self.sender)
        print("To:\t" + recv)
        print("Subject:" + subject)
        print("Contents")
        print(contents)
        print("-"*20)

e = Email()
e.sender = ".....@gmail.com"
recv_list = ['1@gmail.com', '2@gmail.com', '3@gmail.com']

for recv in recv_list:
    e.send_mail(recv, "Welcome!", "This is contents")

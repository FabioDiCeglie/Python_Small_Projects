# OOP
class Email:
    def __init__(self,subject, body, from_recipient):
        # self.to = to
        self.subject = subject
        self.body = body

        # split = from_recipient.split("@")
        # if split[1] != "epicpython.io":
        #     raise Exception("Invalid domain")

        self.__from_recipient = from_recipient

    @property
    def from_recipient(self):
        return self.__from_recipient

    #Modify only from the setter
    @from_recipient.setter
    def from_recipient(self, from_recipient):
        self.__from_recipient = from_recipient
        split = from_recipient.split("@")
        if split[1] != "epicpython.io":
            raise Exception("Invalid domain")

    def send(self, to):
    #    print(f"Sending email with subject: {self.subject} and body: {self.body} to: {self.to}")
     print(f"Sending email from: {self.__from_recipient} with subject: {self.subject} and body: {self.body} to: {to}")



greeting_email = Email("Welcome", "Welcome to epicpython.io", "greeting@epicpython.io")
# greeting_email = Email("Welcome", "Welcome to epicpython.io", "greeting@hello.io") #Error
# greeting_email._from_recipient = "welcome@ciao.com" # here we are not restricted
greeting_email.__from_recipient = "welcome@ciao.com" # here we are restricted because of the __ underscores because it become private but with @property we are not restricted but it will not work
greeting_email.subject = "Greeting"

# print(greeting_email.send())

print(greeting_email.send("ciao.com"))




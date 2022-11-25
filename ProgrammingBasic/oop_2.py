# OOP
class Email:
    valid_domain = "epicpython.io"

    def __init__(self,subject, body, from_recipient):
        # self.to = to
        self.subject = subject
        self.body = body
        self.is_from_recipient_valid(self.valid_domain, from_recipient)

        split = from_recipient.split("@")
        if split[1] != self.valid_domain:
            raise Exception("Invalid domain")

        self.__from_recipient = from_recipient

    @property
    def from_recipient(self):
        return self.__from_recipient

    #Modify only from the setter
    @from_recipient.setter
    def from_recipient(self, from_recipient):
        self.is_from_recipient_valid(self.valid_domain, from_recipient)
        self.__from_recipient = from_recipient

    def send(self, to):
    #    print(f"Sending email with subject: {self.subject} and body: {self.body} to: {self.to}")
         print(f"Sending email from: {self.__from_recipient} with subject: {self.subject} and body: {self.body} to: {to}")

    @classmethod
    def greeting(cls):
        return cls("Welcome!", "Welcome to epicpython.io!", "greeting@epicpython.io")

    @staticmethod
    def is_from_recipient_valid(valid_domain, from_recipient):
        splitted = from_recipient.split("@")
        if splitted[1] != valid_domain:
            raise Exception("Invalid domain")




# greeting_email = Email.greeting()
# bf_email = Email("Black Friday 2022", "50% discount", "bf@epicpython.io")

# Email.valid_domain = "example.com"
# greeting_email = Email("Welcome", "Welcome to epicpython.io", "greeting@hello.io") #Error
# greeting_email._from_recipient = "welcome@ciao.com" # here we are not restricted
# greeting_email.__from_recipient = "welcome@ciao.com" # here we are restricted because of the __ underscores because it become private but with @property we are not restricted but it will not work

# greeting_email.from_recipient = "greeting@example.com"
# bf_email.from_recipient = "bf@example.com"
# greeting_email.subject = "Greeting"

# print(greeting_email.send())
# print(greeting_email.send("ciao.com"))

# print(bf_email.send("alex@gmail.com"))
greeting_email = Email.greeting()
bf_email = Email("Black Friday 2020!", "50% discounts only on our platform, don't miss them!", "bf@epicpython.io")

bf_email.from_recipient = "bf@epicpython.uk"

greeting_email.send("bob@nasa.gov")
bf_email.send("alex@gmail.com")

#it will give an error because the domain is not correct


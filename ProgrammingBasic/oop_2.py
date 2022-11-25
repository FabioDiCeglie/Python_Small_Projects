# OOP
class Email:
    def __init__(self,subject, body):
        # self.to = to
        self.subject = subject
        self.body = body

    def send(self, to):
    #    print(f"Sending email with subject: {self.subject} and body: {self.body} to: {self.to}")
     print(f"Sending email with subject: {self.subject} and body: {self.body} to: {to}")



greeting_email = Email("Welcome", "Welcome OOP")

greeting_email.subject = "Greeting"

# print(greeting_email.send())

print(greeting_email.send("ciao.com"))

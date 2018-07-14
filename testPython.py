#add a name jango.G
template = """
From: <{from_email}>
To: <{to_email}>
Subject: {subject}
{message}"""
print(template.format(
from_email = "a@example.com",
to_email = "b@example.com",
message = "Here's some mail for you. "
" Hope you enjoy the message!",
subject = "You have mail!"
))

emails = ("a@example.com", "b@example.com")
message = {
'subject': "You Have Mail!",
'message': "Here's some mail for you!"
}
template = """
From: <{0[0]}>
To: <{0[1]}>
Subject: {message[subject]}
{message[message]}"""
print(template.format(emails, message=message))

emails = ("a@example.com", "b@example.com")
message = {
'emails': emails,
'subject': "You Have Mail!",
'message': "Here's some mail for you!"
}
template = """
From: <{0[emails][0]}>
To: <{0[emails][1]}>
Subject: {0[subject]}
{0[message]}"""
print(template.format(message))



class EMail:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message
email = EMail("a@example.com", "b@example.com",
"You Have Mail!",
"Here's some mail for you!")
template = """
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}
{0.message}"""
print(template.format(email))


orders = [('burger', 2, 5),
('fries', 3.5, 1),
('cola', 1.75, 3)]
print("PRODUCT  QUANTITY    PRICE   SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print("{0:10s}{1: ^9d} ${2: <8.2f}${3: >7.2f}".format(product, quantity, price, subtotal))


import datetime
print("{0:%Y-%m-%d %I:%M%p }".format(
datetime.datetime.now()))

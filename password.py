class Options(object):
    default_options={
        'port':21,
        'host':'localhost',
        'username':None,
        'password':None,
        'debug':False,
    }
    def __init__(self,**kwargs):
        self.options=dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self,key):
        return self.options[key]


o=Options(username='dusty',password='qwerty')
print(o['debug'],o['port'],o['username'])



import shutil
import os.path
def augmented_move(target_folder, *filenames,verbose=False, **specific):
    '''Move all filenames into the target_folder, allowing
    specific treatment of certain files.'''
    def print_verbose(message, filename):
        '''print the message only if verbose is enabled'''
        if verbose:
            print(message.format(filename))

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        if filename in specific:
            if specific[filename] == 'ignore':
                print_verbose("Ignoring {0}", filename)
            elif specific[filename] == 'copy':
                print_verbose("Copying {0}", filename)
                shutil.copyfile(filename, target_path)
        else:
            print_verbose("Moving {0}", filename)
            shutil.move(filename, target_path)



def show_args(arg1, arg2, arg3="THREE"):
    print(arg1, arg2, arg3)
some_args = range(3)
more_args = {
"arg1": "ONE",
"arg2": "TWO"}
print("Unpacking a sequence:", end=" ")
show_args(*some_args)
print("Unpacking a dict:", end=" ")
show_args(**more_args)


def my_function():
    print("The Function Was Called")
my_function.description = "A silly function"
def second_function():
    print("The second was called")
second_function.description = "A sillier function."
def another_function(function):
    print("The description:", end=" ")
    print(function.description)
    print("The name:", end=" ")
    print(function.__name__)
    print("The class:", end=" ")
    print(function.__class__)
    print("Now I'll call the function passed in")
    function()
another_function(my_function)
another_function(second_function)



import datetime
import time
class TimedEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback
    def ready(self):
        return self.endtime <= datetime.datetime.now()
class Timer:
    def __init__(self):
        self.events = []
    def call_after(self, delay, callback):
        end_time = datetime.datetime.now() + \
        datetime.timedelta(seconds=delay)
        self.events.append(TimedEvent(end_time, callback))
    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)


def format_time(message, *args):
    now = datetime.datetime.now().strftime("%I:%M:%S")
    print(message.format(*args, now=now))
def one(timer):
    format_time("{now}: Called One")
def two(timer):
    format_time("{now}: Called Two")
def three(timer):
    format_time("{now}: Called Three")
# class Repeater:
#     def __init__(self):
#         self.count = 0
#     def repeater(self, timer):
#         format_time("{now}: repeat {0}", self.count)
#         self.count += 1
#         timer.call_after(5, self.repeater)
# timer = Timer()
# timer.call_after(1, one)
# timer.call_after(2, one)
# timer.call_after(2, two)
# timer.call_after(4, two)
# timer.call_after(3, three)
# timer.call_after(6, three)
# repeater = Repeater()
# timer.call_after(5, repeater.repeater)
# format_time("{now}: Starting")
# timer.run()

# class A:
#     def print(self):
#         print("my class is A")
# def fake_print():
#     print("my class is not A")
# a = A()
# a.print()
# a.print = fake_print
# a.print()


# class Repeater:
#     def __init__(self):
#         self.count = 0
#     def __call__(self, timer):
#         format_time("{now}: repeat {0}", self.count)
#         self.count += 1
#         timer.call_after(5, self)
# timer = Timer()
# timer.call_after(5, Repeater())
# format_time("{now}: Starting")
# timer.run()


import smtplib
from email.mime.text import MIMEText
# def send_email(subject, message, from_addr, *to_addrs,host="localhost", port=1025, **headers):
#     email = MIMEText(message)
#     email['Subject'] = subject
#     email['From'] = from_addr
#     for header, value in headers.items():
#         email[header] = value
#     sender = smtplib.SMTP(host, port)
#     for addr in to_addrs:
#         del email['To']
#         email['To'] = addr
#         sender.sendmail(from_addr, addr, email.as_string())
#     sender.quit()
def send_email(subject, message, from_addr, *to_addrs,host="localhost", port=1025, headers=None):
    headers = {} if headers is None else headers
send_email("A model subject", "The message contents","from@example.com", "to1@example.com", "to2@example.com")
from collections import defaultdict
class MailingList:
    '''Manage groups of e-mail addresses for sending e-mails.'''
    def __init__(self):
        self.email_map = defaultdict(set)
    def add_to_group(self, email, group):
        self.email_map[email].add(group)
def emails_in_groups(self, *groups):
    groups = set(groups)
    emails = set()
    for e, g in self.email_map.items():
        if g & groups:
            emails.add(e)
    return emails
def send_mailing(self, subject, message, from_addr,*groups, headers=None):
    emails = self.emails_in_groups(*groups)
    send_email(subject, message, from_addr,*emails, headers=headers)
def save(self):
    with open(self.data_file, 'w') as file:
        for email, groups in self.email_map.items():
            file.write('{} {}\n'.format(email, ','.join(groups)))
def load(self):
    self.email_map = defaultdict(set)
    try:
        with open(self.data_file) as file:
            for line in file:
                email, groups = line.strip().split(' ')
                groups = set(groups.split(','))
                self.email_map[email] = groups
    except IOError:
        pass

def __init__(self, data_file):
    self.data_file = data_file
    self.email_map = defaultdict(set)
def __enter__(self):
    self.load()
    return self
def __exit__(self, type, value, tb):
    self.save()


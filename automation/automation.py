import re, shutil, glob


with open("/Users/kyle/Documents/projects/codefellows/code401Python/automation/automation/potential-contacts.txt") as file:
    potentials = file.read()

phone = []
phone.extend(re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', potentials))

phone_no_dupes = list(set(phone))
phone_sorted = phone_no_dupes.sort()

phone_num_str = ""
for num in phone_no_dupes:
    phone_num_str += num + ", "

with open("/Users/kyle/Documents/projects/codefellows/code401Python/automation/automation/phone_numbers.txt", "w") as file:
    phone_nums = file.write(phone_num_str)

emails = []
emails.extend(re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', potentials))

email_no_dupes = list(set(emails))
emails_sorted = email_no_dupes.sort()

email_str = ""

for email in email_no_dupes:
    email_str += email + " ,"

with open("/Users/kyle/Documents/projects/codefellows/code401Python/automation/automation/emails.txt" ,"w") as file:
    write_email = file.write(email_str)
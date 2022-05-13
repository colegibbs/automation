import re

def find_phones(file):
  with open(file) as f:
    file_text = f.read()

  pattern = r"(\d{3}-|\(\d{3}\)-|)(\d{3}-\d{4})"
  unformated_phones = re.findall(pattern, file_text)
  unformated_phones = [''.join(phone) for phone in unformated_phones]
  formated_phones = list(map(format_phone, unformated_phones))
  formated_phones = set(formated_phones)

  with open("assets/phone_numbers.txt", "w") as f:
    for phone in formated_phones:
      f.write(f"{phone}\n")


def format_phone(phone):
  if len(phone) == 8:
     pre = "206-"
     phone = pre + phone
     return phone
  else:
    return phone

def find_emails(file):
  with open(file) as f:
    file_text = f.read()
  
  pattern = r"([\w\d-]*@[\w\d-]*\.)(com|org|net|gov|edu)"
  emails = re.findall(pattern, file_text)
  
  formatted = [''.join(email) for email in emails]
  formatted = set(formatted)
  email_str = '\n'.join(formatted)
  
  with open("assets/emails.txt", 'w') as f:
    f.write(email_str)


def find_emails_phones(file):
  find_emails(file)
  find_phones(file)

find_emails_phones("assets/potential-contacts.txt")
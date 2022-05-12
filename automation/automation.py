import re

def find_phones(file):
  with open(file) as f:
    file_text = f.read()

  pattern = r"(\d{3}-|\(\d{3}\)-|)(\d{3}-\d{4})"
  unformated_phones = re.findall(pattern, file_text)
  unformated_phones = [''.join(phone) for phone in unformated_phones]
  formated_phones = list(map(format_phone, unformated_phones))
  formated_phones = set(formated_phones)
  print(formated_phones)

  with open("assets/extracted-phones.txt", "w") as f:
    for phone in formated_phones:
      f.write(f"{phone}\n")


def format_phone(phone):
  if len(phone) == 8:
     pre = "206-"
     phone = pre + phone
     return phone
  else:
    return phone

find_phones("assets/potential-contacts.txt")
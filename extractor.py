import re

phone_regex = r"\(?\d{3}\)?[- ]\d{3}[- ]\d{4}"
email_regex = r"([\w\.]+@\w+\.(com|net|org))"
website_regex = r"(^|\s)(\w+\.(com|net|org))"

with open("example_email.txt", "r") as file:
    content = file.read()


phone_matches = re.findall(phone_regex, content)
email_matches = re.findall(email_regex, content, re.IGNORECASE)
website_matches = re.findall(website_regex, content, re.IGNORECASE)


phone_list = []

for phone in phone_matches:
    line = phone + "\n"

    if line not in phone_list:
        phone_list.append(line)

with open("phone_numbers.txt", "w") as file:
    file.writelines(phone_list)


email_list = []

for email in email_matches:
    line = email[0] + "\n"

    if line not in email_list:
        email_list.append(line)

with open("emails.txt", "w") as file:
    file.writelines(email_list)


website_list = []

for website in website_matches:
    line = website[1] + "\n"

    if line not in website_list:
        website_list.append(line)

with open("websites.txt", "w") as file:
    file.writelines(website_list)

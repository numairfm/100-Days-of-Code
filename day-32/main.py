import smtplib
import datetime as dt
import random
import pandas

my_email = "numair@mail.com"
password = ""

date = dt.datetime.now()

month = date.month
day = date.day
today = (month, day)

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

with open("quotes.txt", "r") as f:
    quotes = f.readlines()
    
def replace_name(file, new):
    with open(file, 'r') as f:
        data = f.read()
    
    new_letter = data.replace("[NAME]", new)
    return new_letter
        
def send_birthday_wish():
    data = pandas.read_csv("birthdays.csv")
    
    for i, row in data.iterrows():
        name = row["name"]
        email = row["email"]
        month = row.month
        day = row.day

        if today == (month, day):
            letter = replace_name(random.choice(letters), name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Birthday Letter!\n\n{letter}\n\n{random.choice(quotes)}"
            )
            return True
    return False

send_birthday_wish()

# EXAMPLE OUTPUT

# Hey Mimi,

# Happy birthday! Have a wonderful time today and eat lots of cake!

# Lots of love,

# Numair

# "Don't brood. Get on with living and loving. You don't have forever." - Leo Buscaglia
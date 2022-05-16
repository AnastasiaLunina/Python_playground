import datetime as dt
import pandas
import random
import smtplib

my_email = "lunina.anastasiya@gmail.com"
password = "xbgyeepayanws"

# Checking if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
today_tuple = (now.month, now.day)

# Reading the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# Use dictionary comprehension to create a dictionary from birthday.csv formatted following way:
# birthdays_dict = {(11, 02): Test,test@email.com,2002,11,02}
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# Comparing and see if today's month/day tuple matches one of the keys in birthday_dict.
# If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and
# replace the [NAME] with the person's actual name from birthdays.csv

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # Using the random module to get a number between 1-3 to pick a random letter.
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        # Using the replace() method to replace [NAME] with the actual name
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Making a connection secure
        connection.starttls()
        # Using the connection to log in
        connection.login(user=my_email, password=password)
        # Sending an e-mail
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            # Adding a content by adding \n\n
                            msg=f"Subject:Happy Birthday!\n\n{contents}")




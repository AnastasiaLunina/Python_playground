import smtplib
import datetime as dt
import random


my_email = "lunina.anastasiya@gmail.com"
# If you use google, you need to generate app password for Windows Computer because gmail does not allow the application
# access account by default for security purposes
# https://support.google.com/accounts/answer/185833?visit_id=637882520682140480-1498968666&p=InvalidSecondFactor&rd=1
# https://myaccount.google.com/security
# Then under Signing in to Google and App passwords create App password
password = "xbgyeefmpayanwse"
# First we need to figure out day of the week now
# By first figuring out the full date and then finding a weekday
now = dt.datetime.now()
weekday = now.weekday()
# Next if the weekday is Monday (or any other day of your choice, we are going to send an email
# For that we need to read our quotes.txt file and choose the random quote to send, using a random module
if weekday == 6:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
# Next we need to create a connection using smtplib and SMTP class and provide the url of the host
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Making a connection secure
        connection.starttls()
        # Using the connection to log in
        connection.login(user=my_email, password=password)
        # Sending an e-mail
        connection.sendmail(from_addr=my_email,
                            to_addrs="mishol03@yahoo.com",
                            # Adding a content by adding \n\n
                            msg=f"Subject:Sunday Motivation\n\n{quote}")
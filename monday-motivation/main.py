import datetime as dt
import smtplib
import random

day = dt.datetime.today()
weekday = day.weekday()
print(weekday)
user_mail = "Your Mail ID"      #Enter your Mail Id
password = "Your Mail Password" #Enter your Mail Password
if weekday == 0:
    print("Yes")
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote_of_day = random.choice(all_quotes)
        print(quote_of_day)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:    #Note: I have used smtp for gmail if your from address has different mail id then use respective smtp
        connection.starttls()
        connection.login(user=user_mail, password=password)
        print("YES")
        connection.sendmail(
            from_addr=user_mail,
            to_addrs=user_mail,
            msg=f"Subject:Your Motivation for today\n\n{quote_of_day}"
        )
else:
    print("Failed")


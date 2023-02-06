import smtplib
import base64

filename = "files/classes data/In"
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

fo = open(filename,"rb")


smtpObj.starttls()

smtpObj.login("asatdreamz@gmail.com", "Only_business2004")
sender = "asatdreamz@gmail.com"
receiver = ["bhatsaab04@gmail.com"]

message = """From: Admini <asatdreamz@gmail.com>
To: To Person <bhatsaab04@gmail.com>
Subject: SMTP test

The OTP is 5406.
"""

smtpObj.sendmail(sender, receiver, message)
print("Success")
smtpObj.quit()
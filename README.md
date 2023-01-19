# Autoemail
code to send automatic emails

# Description
This Python script utilizes the Simple Mail Transfer Protocol (SMTP) to send emails from a specific email address to a list of recipients. The smtplib library is used to interact with the email server and establish a secure connection using the starttls() method. It's important to note that you need to use your own email address and password in the code, and may need to enable less secure apps in your email account settings to use the script. To make the email look more professional, subject and properly formatting the message with a body and signature using the MIMEMultipart and MIMEText classes from the email library.

# Installation

$ git clone https://github.com/subgqg/autoemail.git/

$ cd autoemail

$ python3 -m pip install -r requirments.txt

$ python3 emailsender.py

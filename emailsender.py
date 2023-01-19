import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Login to the email server
sender_email = "myemail@gmail.com"
password = "mypassword"
server.login(sender_email, password)

# List of recipients
recipients = ["classmember1@email.com", "classmember2@email.com", "classmember3@email.com", "familymember1@email.com", "familymember2@email.com"]

# Create the message structure
msg = MIMEMultipart()

# Add the subject
msg['Subject'] = "Automatic Email from Python Script"

# Add the body
body = "Hello, \n\n This is an automatic email sent from my python script. \n\n Best Regards,\n Your Name"
msg.attach(MIMEText(body, 'plain'))

# Add the signature
signature = "Your Name\nYour Title\nYour Company"
msg.attach(MIMEText(signature, 'plain'))

# Send the email
server.sendmail(sender_email, recipients, message)

# Disconnect from the server
server.quit()

#import libraries needed
from email.message import EmailMessage
from app2 import password

# Set up email details
email_sender = 'morgandavid261@gmail.com'
email_password = password

# Specify multiple recipients
email_receiver = ['ooregunwa@gmail.com', 'beckhamoregunwa@gmail.com']

#create the subject and body of the email using variables
subject="INTERVIEW QUESTIONS AND ANSWER(REVISED)"
body = """
"""
   
# Create an EmailMessage instance and set its headers and content
em = EmailMessage()
em['From'] = email_sender
em['TO'] = ', '.join(email_receiver)# Join the list of email addresses into a single string
em['subject'] = subject
em.set_content(body) #Here we specify the content of the email message to be the body variable created

#To create context of the email we have to import ssl and smtp
import ssl
import smtplib

#Creating a context variable to allow ssl create default context
context = ssl.create_default_context()

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)  # Log into SMTP server
    smtp.send_message(em)  # Use send_message instead of sendmail
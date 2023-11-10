# Email-Sender
 # Automated Email Sender

This project provides a simple and secure tool for sending automated emails using the `smtplib` library and Gmail. It allows users to easily configure and send emails without the need for complex programming or external services.

## Features

- Easy-to-use interface
- Secure email sending with SSL encryption
- Configurable email content
- No external dependencies

## Requirements

- Python 3.x
- SSL library
- `smtplib` library

## Installation

### To install the tool, simply clone the repository and install the dependencies:

```bash
git clone https://github.com/<your-username>/automated-email-sender.git
cd automated-email-sender
pip install -r requirements.txt
```

## Usage

### To send an email, create a Python script and import the necessary libraries:

```python
from email.message import EmailMessage
from ssl import create_default_context
import smtplib
```
### Set up the email sender's information:

```python
email_sender = 'your_email_address@gmail.com'
email_password = 'your_password'
```
### Create the email message:

```python
subject = 'Your Email Subject'
body = 'Your Email Body'

em = EmailMessage()
em['From'] = email_sender
em['TO'] = ', '.join(email_receiver)
em['subject'] = subject
em.set_content(body)
```
### Connect to the Gmail server and send the email:

```python
context = create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
```
## Example Usage
```python
from email.message import EmailMessage
from ssl import create_default_context
import smtplib

# Set up email sender's information
email_sender = 'morgandavid261@gmail.com'
email_password = 'password'

# Specify recipient email addresses

email_receiver = ['ooregunwa@gmail.com', 'beckhamoregunwa@gmail.com']


# Specify email subject and body
subject = 'INTERVIEW QUESTIONS AND ANSWER(REVISED)'
body = """
# Interview Questions

1. What is your favorite programming language?
2. Tell me about a time when you faced a challenging problem and how you resolved it.
3. ...

# Answers

1. My favorite programming language is Python because...
2. When I faced a challenging problem...
3. ...
"""

# Create the email message
em = EmailMessage()
em['From'] = email_sender
em['TO'] = ', '.join(email_receiver)
em['subject'] = subject
em.set_content(body)

# Connect to the Gmail server and send the email
context = create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
```

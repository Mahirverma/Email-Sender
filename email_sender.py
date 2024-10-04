import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('index.html').read_text())
email=EmailMessage()
email['From']='Sender-email-address'
email['To']='Receiver-email-address'
email['Subject']='Write-down-your-subject'
email.set_content(html.substitute({'name':'name-of-your-recipient'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your-gmail-address', 'your-third-party-app-address')
    smtp.send_message(email)
    print("All good!")
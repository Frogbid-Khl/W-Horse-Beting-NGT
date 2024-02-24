import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

sender_email = 'noreply@frogbid.com'
receiver_email = 'frogbidofficial@gmail.com'
subject = 'HKJC Python'
body = 'Python Stop. Please Run it Quickly or Clifton Will be very angry!'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

message.attach(MIMEText(body, 'plain'))

smtp_server = 'mail.frogbid.com'
smtp_port = 465
username = 'noreply@frogbid.com'
password = 'h3m(%@e1165_'

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
    server.login(username, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")

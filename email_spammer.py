# SMTP email command line client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def sendEmail(email_from, email_to, password, subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_from, password)
    server.sendmail(email_from, email_to, text)
    server.quit()
    print("Email sent")

def spamEmail(email_from, email_to, password, subject, body, num_emails):
    for i in range(num_emails):
        sendEmail(email_from, email_to, password, subject, body)

def main():
    email_from = input("Enter your email: ")
    email_to = input("Enter the email you want to send to: ")
    password = input("Enter your password: ")
    subject = input("Enter the subject: ")
    body = input("Enter the body: ")
    num_emails = int(input("Enter the number of emails you want to send: "))
    spamEmail(email_from, email_to, password, subject, body, num_emails)

if __name__ == "__main__":
    main()
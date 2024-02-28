import smtplib
from email.mime.text import MIMEText
def send_email(email_to, subject, body):
    email_from = 'sonuyohannan4@gmail.com'
    message = MIMEText(body)
    message['From'] = email_from
    message['To'] = ', '.join(email_to)
    message['Subject'] = subject

    EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
    EMAIL_HOST_USER = '675589bad02536'
    EMAIL_HOST_PASSWORD = '638254cf2e8cf7'
    EMAIL_PORT = 2525

    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(email_from, email_to, message.as_string())
    server.quit()
    
email_recipients = ['akp087@gmail.com','dhanu@gmail.com','blublu@gmail.com']
subject = 'Communication about enquiry'
body = 'Dear recipient, I hope this email finds you well.'

send_email(email_recipients, subject, body)

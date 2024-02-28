import smtplib
from email.mime.text import MIMEText
 
def send_email(email_from, email_to, subject, body):
    message = MIMEText(body)
    message['From'] = email_from
    message['To'] = ', '.join(email_to)
    message['Subject'] = subject
 
    EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
    EMAIL_HOST_USER = '675589bad02536'
    EMAIL_HOST_PASSWORD = '638254cf2e8cf7'
    EMAIL_PORT = '2525'
 
    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(email_from, email_to, message.as_string())
 
        print("Email sent successfully!")
 
    except smtplib.SMTPException as e:
        print(f"SMTP Exception: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
 
if __name__ == "__main__":
    try:
        email_from = 'sonuyohannan4@gmail.com'
        recipients = ['dhanu@gmail.com', 'akp07@gmail.com']
        subject = 'sampletesting'
        body = 'Hello everyone, this is a sample testing email.'
 
        # Send email to multiple recipients
        send_email(email_from, recipients, subject, body)
 
    except Exception as e:
        print(f"An error occurred: {e}")
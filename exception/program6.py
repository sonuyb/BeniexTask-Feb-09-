import smtplib
from email.mime.text import MIMEText
email_from='sonuyohannan4@gmail.com'
email_to='akp087@gmail.com'
subject='communication about enquiry'
body='dear akp,I hope this email finds you well'
message=MIMEText(body)
message['From']=email_from
message['To']=email_to
message['Subject']=subject
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '675589bad02536'
EMAIL_HOST_PASSWORD = '638254cf2e8cf7'
EMAIL_PORT = '2525'
server=smtplib.SMTP(EMAIL_HOST,EMAIL_PORT)
server.starttls()
server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
server.sendmail(email_from,email_to,message.as_string())
server.quit()

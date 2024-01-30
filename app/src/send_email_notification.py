import smtplib
from email.mime.text import MIMEText

# def send_email(subject, body, to):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = 'your-email@gmail.com'
#     msg['To'] = to

#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.login('your-email@gmail.com', 'your-password')  # Use OAuth token if available
#     server.send_message(msg)
#     server.quit()

# @app.get("/send-email/")
# async def send_email_route():
#     send_email("Subject", "Email Body", "recipient@example.com")
#     return {"message": "Email sent"}
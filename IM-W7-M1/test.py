import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, from_email, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", e)

# Email configuration
subject = "Test Email"
body = "This is a test email sent using Python."
from_email = "
your_email@example.com
"
to_email = "
recipient@example.com
"
smtp_server = "
smtp.example.com
"
smtp_port = 587  # Change this to the appropriate SMTP port
smtp_username = "
your_email@example.com
"
smtp_password = "your_email_password"

# Send the email
send_email(subject, body, from_email, to_email, smtp_server, smtp_port, smtp_username, smtp_password) 
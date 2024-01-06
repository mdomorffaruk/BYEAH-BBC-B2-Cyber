
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def sentEmail():
    # sender_email = email_from_entry.get()
    sender_email = "mdomorffaruk@gmail.com"
    
    smtp_server= "smtp.gmail.com"
    smtp_port=465
    sender_auth_key="YOUR)EMAIL_AUTH_KEY"

    # Data from input: 
    recipients_email = input("Enter email: ")
    subject = input("Enter email subject")
    message = input("Enter message")

    try:
        # Connect to the SMTP server
        smtp_connection = smtplib.SMTP_SSL(smtp_server, smtp_port)
        # smtp_connection.starttls()

        # Log in to the SMTP server
        smtp_connection.login(sender_email, sender_auth_key)

        # Compose the email
        email_content = MIMEMultipart()
        email_content['Subject'] = subject
        email_content['From'] = sender_email
        email_content['To'] = ', '.join(recipients_email)
        email_content.attach(MIMEText(message))
        
            # attach_file_to_email(email_content, attach_label.cget("text"))
        file = input("Enter file dir: ")
        attachment = open(file, 'rb')
        obj = MIMEBase('application','octet-stream')
        obj.set_payload((attachment).read())
        encoders.encode_base64(obj)
        obj.add_header('Content-Disposition',"attachment; filename= "+file)
        email_content.attach(obj)

            


        # Send the email
        smtp_connection.sendmail(sender_email, recipients_email, email_content.as_string())

        smtp_connection.quit()
        # messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        print(str(e))
        # messagebox.showerror("Error", f"An error occurred: {str(e)}")
    print("We are trying to sent email...")




sentEmail()

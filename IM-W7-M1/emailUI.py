# import turtle as tur
import tkinter as tk
import smtplib
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from tkinter import filedialog
from email import encoders

HEIGHT=300
WIDTH=400


root = tk.Tk()
root.title("Email Interface")
root.geometry(f"{WIDTH}x{HEIGHT}")



def sentEmail():
    # sender_email = email_from_entry.get()
    sender_email = "mdomorffaruk@gmail.com"
    
    smtp_server= "smtp.gmail.com"
    smtp_port=465
    sender_auth_key="mnhdnepqigtjxqwe"

    # Data from input: 
    recipients_email = email_to_entry.get()
    subject = subject_text.get("1.0", "end-1c")
    message = message_text.get("1.0", "end-1c")

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
        if attach_label is not None:
            # attach_file_to_email(email_content, attach_label.cget("text"))
            file = attach_label.cget("text")
            attachment = open(file, 'rb')
            obj = MIMEBase('application','octet-stream')
            obj.set_payload((attachment).read())
            encoders.encode_base64(obj)
            obj.add_header('Content-Disposition',"attachment; filename= "+file)
            email_content.attach(obj)

            


        # Send the email
        smtp_connection.sendmail(sender_email, recipients_email, email_content.as_string())

        smtp_connection.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    print("We are trying to sent email...")


def exitProgram():
    exit()

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    attach_label.config(text=filename)


email_to_label = tk.Label(root, text="Email To:")
email_to_label.pack(side='top', anchor='nw', padx=10 )
email_to_entry = tk.Entry(root,  width=40)
email_to_entry.pack(side='top', anchor='nw', padx=10)

subject_label = tk.Label(root, text="Subject:")
subject_label.pack(side='top', anchor='nw', padx=10)
subject_text = tk.Text(root, height=2, width=45)
subject_text.pack(side='top', anchor='nw', padx=10)

# Create a label and text widget for the Message
message_label = tk.Label(root, text="Message:")
message_label.pack(side='top', anchor='nw', padx=10)
message_text = tk.Text(root, height=5, width=45)
message_text.pack(side='top', anchor='nw', padx=10)





attach_label = tk.Label(root, text=None)
attach_label.pack(side='top', anchor='nw', padx=10)
attach_button = tk.Button(root, text='Attach a file', command=UploadAction)
attach_button.pack(side='left', anchor='nw', padx=20)

send_button = tk.Button(root, text="Send Email", command=sentEmail)
send_button.pack(side='left', anchor='nw', padx=20)

exit_button = tk.Button(root, text="Exit", command=exitProgram)
exit_button.pack(side='top', anchor='nw', padx=20)





root.mainloop()




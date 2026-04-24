import smtplib
def send_email(alert_msg):
    sender = "dhallp777@gmail.com"
    reciever = "dhallpre999@gmail.com"
    password = "cqcy jaqc eiwl xtim"
    message = f"Subject: Sales Alert\n\n{alert_msg}"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, reciever, message)
        server.quit()
        print("Email sent Successfully!")
    except Exception as e:
        print("Email Failed", e)
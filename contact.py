import smtplib

def send_email(name, email, message, subject):
    yahoopass = "vzksfrmmeajybatk"
    my_email = "gabrielcolli.sr@yahoo.com"
    with smtplib.SMTP("smtp.mail.yahoo.com", port = 587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = yahoopass)
        connection.sendmail(from_addr = my_email, to_addrs = "python.sparkon@gmail.com", msg = f"Subject: {subject}\n\n{name}\n{email} has sent you a message:\n\n{message}")
                
                    
               
        
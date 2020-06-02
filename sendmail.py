import json
import smtplib
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Enable Less secure app access
# https://myaccount.google.com/lesssecureapps
def sendmail(subject, body, reciever_mail, json_data):
    try:
        cp = configparser.ConfigParser()
        cp.read('settings.ini')
    except Exception as e:
        print("Exception in reading settings.ini file" + str(e))
    else:
        # print(cp.get("SMTP", "hostname"), cp.get("SMTP", "sender_mail"), cp.get("SMTP", "password"))
        sender_mail = cp.get("SMTP", "sender_mail")
        hostname = cp.get("SMTP", "hostname")
        password = cp.get("SMTP", "password")
        with smtplib.SMTP(hostname) as server:
            server.starttls()
            server.login(sender_mail, password)
            msg = MIMEMultipart('alternative')
            msg['From'] = sender_mail
            msg['To'] = reciever_mail
            msg['Subject'] = subject
            body = MIMEText(body, "plain")
            attachment = MIMEText(json_data, 'plain')
            attachment.add_header('Content-Disposition', 'attachment', filename='searchResults.json')
            msg.attach(body)
            msg.attach(attachment)
            server.send_message(msg)
            # server.sendmail(
            #     from_address,
            #     reciever_mail,
            #     msg.as_string(),
            # )
        print("Success!")

# if __name__ == '__main__':
    # json_data = '{"ID": 2, "name": "venkatesh23"}'
    # sendmail('Search Results', 'PFA Results', 'venkatesh23.ch@gmail.com', json_data)
import os
import sys
import datetime
import smtplib
import logging
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

now = datetime.datetime.now()

logging.basicConfig(filename='logger.txt', level=logging.DEBUG)

# Link directories to read in credentials
LOGGING_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(LOGGING_DIR))
PERSONAL_DIR = os.path.join(BASE_DIR, 'Personal')

sys.path.append(PERSONAL_DIR)

# TODO - Add this to a configuration file somewhere, probably JSON
from settings import EMAIL_HOST, EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, EMAIL_PORT, EMAIL_USE_SSL, EMAIL_USE_TLS

def format_header():
    formatted_date_pattern = '%A, %m/%d/%y'
    date_time_today = datetime.datetime.today()
    formatted_today = date_time_today.strftime(formatted_date_pattern)
    formatted_header = 'Today\'s Logging Notes for {}'.format(formatted_today)
    return formatted_header

def send_daily_logs():
    # Grab Log File
    logging_file = open('logger.txt', 'r', encoding='utf-8')

    # Create a new string
    temp_file = ''
    temp_file += '\n--------------------Begin Logs--------------------\n\n'

    # Bring in formatted header
    formatted_header = format_header()

    # Append to the string
    temp_file += logging_file.read()


    receipients = [EMAIL_HOST_USER, 'Jarret.Laberdee@fcagroup.com']


    for recipient in receipients:
            # Format Email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = recipient
        msg['Subject'] = formatted_header

        # Attach message as plain text
        msg.attach(MIMEText(temp_file, 'plain'))

        attached_logs = open('logger.txt', 'rb')
        filename = formatted_header

        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload((attached_logs).read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', "attachment; filename={}".format(filename))

        msg.attach(attachment)

        body = msg.as_string()

        # Log into the server
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.connect(EMAIL_HOST, EMAIL_PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

        # Send the email
        server.sendmail(EMAIL_HOST_USER, recipient, body)
        logging.info('\nEmail Sent To {} at {}'.format(recipient, now))
        server.quit()

        # Close Files
        logging_file.close()
        attached_logs.close()

send_daily_logs()
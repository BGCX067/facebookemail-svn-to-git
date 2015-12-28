'''
Created on Jul 26, 2012

@author: aakashj
'''

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText("aakash jain email")
#fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of '
msg['From'] = "IAC"
msg['To'] = "jaaksah2004@gmail.com"

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP()
s.sendmail("jaaksah@python.com","aakash.jain@citrix.com", msg.as_string())
s.quit()
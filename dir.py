import os
import time
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

path_to_watch = "D:\Daily-files"
print ("watching: " + path_to_watch)
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if removed: print ("Removed: ", ", ".join (removed))
    if added:
        print ("Added: ", ", ".join (added))
        me = "edia@gvcplc.com"
        you = "edia@gvcplc.com"
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "New file has approached."
        msg['From'] = me
        msg['To'] = you
        text = "new files Added"
        part1 = MIMEText(text, 'plain')
        msg.attach(part1)
        mailserver = smtplib.SMTP('smtp.office365.com',587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login('edia@gvcplc.com', 'Leon21013@')
        mailserver.sendmail(me, you, msg.as_string())
        mailserver.quit()
    time.sleep (10)
    before = after
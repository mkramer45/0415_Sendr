import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sqlite3
import sys
#sys.setdefaultencoding('utf8')

# select random msg
conn = sqlite3.connect('StriveDB2.db')
cursor = conn.cursor()
cur2 = cursor.execute('SELECT quote, RecordID FROM Funny ORDER BY RANDOM() LIMIT 1;')
info2 = cur2.fetchone()
conn.commit()
conn.close()
conn.close()

#msg
j = info2[0]
#recordID
k = info2[1]

# select email addresses as list to send to
conn5 = sqlite3.connect('StriveDB2.db')
cursor5 = conn5.cursor()
cur5 = cursor5.execute('SELECT email FROM Sendr_Usr WHERE RadioB = "Funny"')
info5 = cur5.fetchall()
conn5.commit()
conn5.close()
conn5.close()

newlist = [row[0] for row in info5]


msg = MIMEMultipart()
msg['From'] = 'mkramer265@gmail.com'
msg['To'] = 'mkramer789@gmail.com'
msg['Subject'] = 'Funny'
message = j
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('mkramer265@gmail.com', 'Celtics123')

mailserver.sendmail('mkramer265@gmail.com',newlist,msg.as_string())

mailserver.quit()

connx = sqlite3.connect('StriveDB2.db')
cursorx = connx.cursor()
curx = cursorx.execute("INSERT INTO RIDX VALUES (?)", (k,))
connx.commit()
cursorx.close()
connx.close()

print(j)
print(newlist)
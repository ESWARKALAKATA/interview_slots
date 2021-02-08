import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os,datetime
from jinja2 import Template

CRLF = "\r\n"
login = "eswar.bbid@gmail.com"
password =  "eswar@1234"
attendees = ["eswar.py@outlook.com"]
organizer = "ORGANIZER;Eswar:mailto:eswar.kalakata"+CRLF+" @gmail.com"
fro = "eswar <eswar.chotu247@gmail.com>"

ddtstart = datetime.datetime.now()
dtoff = datetime.timedelta(days = 1)
dur = datetime.timedelta(hours = 1)
ddtstart = ddtstart +dtoff
dtend = ddtstart + dur
dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
dtend = dtend.strftime("%Y%m%dT%H%M%SZ")

description = "DESCRIPTION: test invitation from  Eswar pyICSParser"+CRLF
attendee = ""
for att in attendees:
    attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE"+CRLF+" ;CN="+att+";X-NUM-GUESTS=0:"+CRLF+" mailto:"+att+CRLF
ical = "BEGIN:VCALENDAR"+CRLF+"PRODID:pyICSParser"+CRLF+"VERSION:2.0"+CRLF+"CALSCALE:GREGORIAN"+CRLF
ical+="METHOD:REQUEST"+CRLF+"BEGIN:VEVENT"+CRLF+"DTSTART:"+dtstart+CRLF+"DTEND:"+dtend+CRLF+"DTSTAMP:"+dtstamp+CRLF+organizer+CRLF
ical+= "UID:FIXMEUID"+dtstamp+CRLF
ical+= attendee+"CREATED:"+dtstamp+CRLF+description+"LAST-MODIFIED:"+dtstamp+CRLF+"LOCATION:"+CRLF+"SEQUENCE:0"+CRLF+"STATUS:CONFIRMED"+CRLF
ical+= "SUMMARY:Interview@map_recriut "+ddtstart.strftime("%Y%m%d @ %H:%M")+CRLF+"TRANSP:OPAQUE"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF

eml_body = '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

    <title></title>
  </head>
  <body>
    <div class = "container">
        <p style="color:rgb(30, 255, 0)">You have been invited to the following event</p>

        <h1>{{ subject }}</h1>
        <table  class="table table-borderless">
            <tbody>
            <tr>
                <td>when</td>
                <td>Fri 29 Jan 2021 9:30am – 10:30am Coordinated Universal Time</td>
        
            </tr>
            <tr>
                <td>calender</td>
                <td>{{ att }}</td>
            
            </tr>
            <tr>
                <td >Who</td>
                <td><ul>
                    <li>{{ log }}</li>
                </ul> 
                </td>
            </tr>
            </tbody>
      </table>
    </div>

     <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>
    -->
  </body>
</html>
'''
tm  = Template(eml_body)
body  = tm.render(subject = "Eswar invite @"+dtstart,att = attendees[0],log = login )
eml_body_bin = "This is the email body in binary - two steps"
msg = MIMEMultipart('mixed')
msg['Reply-To']=fro
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = "Eswar invite @"+dtstart
msg['From'] = fro
msg['To'] = ",".join(attendees)

part_email = MIMEText(body,"html")
part_cal = MIMEText(ical,'calendar;method=REQUEST')

msgAlternative = MIMEMultipart('alternative')
msg.attach(msgAlternative)

ical_atch = MIMEBase('application/ics',' ;name="%s"'%("invite.ics"))
ical_atch.set_payload(ical)
#encoders.encode_base64(ical_atch)
ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"'%("invite.ics"))

eml_atch = MIMEBase('text/plain','')
#encoders.encode_base64(eml_atch)
eml_atch.add_header('Content-Transfer-Encoding', "")

msgAlternative.attach(part_email)
msgAlternative.attach(part_cal)

mailServer = smtplib.SMTP('smtp.gmail.com', 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(login, password)
mailServer.sendmail(fro, attendees, msg.as_string())
mailServer.close()
import email
import smtplib
import datetime as dt
import icalendar
import pytz
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os,datetime
from datetime import date 

today = date.today() 
print(type(today))

# Imagine this function is part of a class which provides the necessary config data
def send_appointment(date, attendee_email, organiser_email, subj, description, location, start_hour, start_minute):
  # Timezone to use for our dates - change as needed
  tz = pytz.timezone("Europe/London")
  start = tz.localize(dt.datetime.combine(date, dt.time(start_hour, start_minute, 0)))
  # Build the event itself
  cal = icalendar.Calendar()
  cal.add('prodid', '-//My calendar application//example.com//')
  cal.add('version', '2.0')
  cal.add('method', "REQUEST")
  event = icalendar.Event()
  event.add('attendee', attendee_email)
  event.add('organizer', organiser_email)
  event.add('status', "confirmed")
  event.add('category', "Event")
  event.add('summary', subj)
  event.add('description', description)
  event.add('location', location)
  event.add('dtstart', start)
  event.add('dtend', tz.localize(dt.datetime.combine(date, dt.time(start_hour + 1, start_minute, 0))))
  event.add('dtstamp', tz.localize(dt.datetime.combine(date, dt.time(6, 0, 0))))
  #event['uid'] = self.get_unique_id() # Generate some unique ID
  event.add('priority', 5)
  event.add('sequence', 1)
  event.add('created', tz.localize(dt.datetime.now()))

  # Add a reminder
  alarm = icalendar.Alarm()
  alarm.add("action", "DISPLAY")
  alarm.add('description', "Reminder")
  # The only way to convince Outlook to do it correctly
  alarm.add("TRIGGER;RELATED=START", "-PT{0}H".format(24)) #reminder_hours
  event.add_component(alarm)
  cal.add_component(event)

  # Build the email message and attach the event to it
  msg = MIMEMultipart("alternative")

  msg["Subject"] = subj
  msg["From"] = organiser_email
  msg["To"] = attendee_email
  msg["Content-class"] = "urn:content-classes:calendarmessage"

  msg.attach(MIMEText(description))
  part_email = MIMEText('calendar;method=REQUEST') #this lines are for 
  msg.attach(part_email)                          # outlook make it as calender   #remove this lines for sending mail to gmail
  filename = "invite.ics"
  part = MIMEBase('text', "calendar", method="REQUEST", name=filename)
  part.set_payload( cal.to_ical() )
  email.encoders.encode_base64(part)
  part.add_header('Content-Disposition', filename)  #content discription
  part.add_header("Content-class", "urn:content-classes:calendarmessage")
  part.add_header("Filename", filename)
  part.add_header("Path", filename)
  msg.attach(part)

  # Send the email out
  s = smtplib.SMTP('smtp.gmail.com',587)
  s.starttls()
  s.login("eswar.bbid@gmail.com","eswar@1234")
  s.sendmail(msg["From"], [msg["To"]], msg.as_string())
  s.quit()



send_appointment(date = today,attendee_email="eswar.kalakata@gmail.com",organiser_email="eswar.bbid@gmail.com",subj="python_practice",description="outlook calender should be done ",location="madhapur",start_hour= 1, start_minute= 55)
'''import pytz
for tz in pytz.all_timezones:
    print(tz)'''



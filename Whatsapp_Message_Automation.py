from twilio.rest import Client
from datetime import datetime,timedelta
import time

account_sid = "OWN SID"
auth_token = "OWN TOKEN"

client = Client(account_sid, auth_token)

def send_message(recepient_number, message_body):
    try:
        message = client.messages.create(
            from_ = 'whatsapp: USER NUM ',
            body = message_body,
            to=f'whatsapp:{recepient_number}'
        )
        print(f"Message sent successfully! Message SID {message.sid}")
    except Exception as e :
        print("An error occured !")

name = input("Enter the recepient name: ")
recepient_number = input("Enter the recepient number +91: ")
message_body = input(f"Enter the message to {name}: ")

date_str = input("Enter the date to send message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM) in 24 hr Format: ")

schedule = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_time = datetime.now()

differ = schedule - current_time
delay_sec = differ.total_seconds()

if delay_sec<=0:
    print("The time you specified is past. Please enter a future date and time... ")
else:
    print(f"Message scheduled to be sent to {name} at {schedule}")

    time.sleep(delay_sec)

    send_message(recepient_number,message_body)

use_sid  = "AC2ec371dd29e2f361823ca4faadcbbf4f"
use_token = "867de2a89cf4fbc39e414d5ad875b420"
num="+14155238886"
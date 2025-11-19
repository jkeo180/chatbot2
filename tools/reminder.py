import time
from datetime import datetime, timedelta

events = { 'event_name' : 'Meeting with team', 'event_time' : datetime.now() + timedelta(minutes=30)}
reminder_times = datetime.now() + timedelta(minutes=1), datetime.now() + timedelta(minutes=60)

add_event = (events["event_name"], events["event_time"])
modify_event = (events["event_name"], events["event_time"] + timedelta(minutes=15))
view_event = (events["event_name"], events["event_time"])
delete_event = (events["event_name"],)
while True:
    current_time = datetime.now()
    for reminder_time in reminder_times:
        if current_time >= reminder_time:
            print(f"Reminder: It's now {current_time.strftime('%Y-%m-%d %H:%M:%S')} get up and stretch!")
            reminder_times = tuple(rt for rt in reminder_times if rt != reminder_time)
    time.sleep(30)  # Check every 30 seconds

    break
else:
    print("All reminders have been sent.")
exit()
print(f"Adding event: {add_event[0]} at {add_event[1].strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Modifying event: {modify_event[0]} to new time {modify_event[1].strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Viewing event: {view_event[0]} at {view_event[1].strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Deleting event: {delete_event[0]}") 
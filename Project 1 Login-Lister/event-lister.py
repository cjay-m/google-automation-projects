from collections import defaultdict

# define the Event object
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

# get function in order to get dates of the event list
def get_event_date(event):
    return event.date

# find the current users that are logged in using conditional statements and the previous event log, this allows us to 
# go through the machines list and output logged in users
def current_users(events):
    events.sort(key = get_event_date)
    machines = defaultdict(list)

    for event in events:
        if event.type == "login":
            if event.user not in machines[event.machine]:
                machines[event.machine].append(event.user)
        elif event.type == "logout":
            if event.user in machines[event.machine]: 
                machines[event.machine].remove(event.user)

    return machines

def generate_report(machines):
    for machine in machines.items():
        if len(users) > 0:
            user_list= ", ".join(users)
            print("{}: {}".format(machine, user_list))


events = [

    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),

]

users = current_users(events)
print(users)


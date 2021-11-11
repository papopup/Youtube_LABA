
from ipaddress import IPv4Address  # for your IP address
from pyairmore.request import AirmoreSession  # to create an AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages

device_ip = IPv4Address("192.168.0.194")  # let's create an IP address object
# now create a session
session = AirmoreSession(device_ip)
# if your port is not 2333
# session = AirmoreSession(ip, 2334)  # assuming it is 2334

session.is_server_running  # True if Airmore is running

was_accepted = session.request_authorization()

print(was_accepted)  # True if accepted


#service = MessagingService(session)

#service.send_message("phone number", "message content")
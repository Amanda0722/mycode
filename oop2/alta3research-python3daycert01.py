#!/usr/bin/python3
#show current time
#A.R. 20220526v1
from datetime import datetime

now = datetime.now()
#UTC time
current_time = now.strftime("%H:%M:%S")
print("Current UTC Time =", current_time)


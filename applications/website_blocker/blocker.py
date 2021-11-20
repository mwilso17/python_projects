# Mike Wilson 18 November 2021
# This is a program that blocks websites (as determined by the user) during certain hours
# For this example, I am using Reddit.com and blocking from 5am until 7am.
# Path for host varies based on OS. C:\Windows\System32\drivers\etc then select host works for Windows.
# As the program is currently set with host_temp, it will write contents in the websites list to the file path
# applications\website_blocker\hosts during the hours of 5am and 7am and erase them outside of those hours. 
# Repacing the 2 uses of host_temp with host_path in the while loop will allow
# for full functionality of the program. User may need to allow permissions for host_path folders.

import time
from datetime import datetime as dt

# Establish host path. host_path may vary on computer and is currently set up for Windows OS.
host_temp = "applications\website_blocker\hosts"
host_path = "C:\Windows\System32\drivers\etc\hosts"

# Redirects to the following IP address, which should be the local host.
redirect = "127.0.0.1"

# List of websites to block
websites = ["www.reddit.com", "reddit.com"]


while True:
  # hours of the day are set at 5 and 7 to denote 5am and 7am local time. These can be adjusted based on a 24 hour clock.
  if dt(dt.now().year, dt.now().month, dt.now().day, 5) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 7):
    # replace host_temp with host_path for full functionality
    with open(host_temp, 'r+') as file:
      content=file.read()
      for website in websites:
        if website in content:
          pass
        else:
          file.write(redirect + " " + website + "\n")
  else:
    # replace host_temp with host_path for full functionality
    with open(host_temp, 'r+') as file:
      content = file.readlines()
      file.seek(0)
      for line in content:
        if not any(website in line for website in websites):
          file.write(line)
      file.truncate()



  # Sets program to update every 60 seconds. Set to 60 seconds to limit use of memory while program active.
  time.sleep(60)

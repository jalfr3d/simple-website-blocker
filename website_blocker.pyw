import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
# You can add or remove url in this list
website_lists = ["www.facebook.com", "facebook.com", "es-la.facebook.com"]

while True:
    # Change the numbers, it set to 8 AM to 20 PM BLOCK
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year,
                                                                          dt.now().month, dt.now().day, 20):
        print("Working hours...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
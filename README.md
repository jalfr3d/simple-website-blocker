# Website Blocker

## Overview

This repository contains a simple Python script that allows you to block access to specific websites during certain time periods. The script modifies your computer's host file to restrict access to the specified websites during working hours and restores access during non-working hours.

## How It Works

The website blocker script operates as follows:

- You provide a list of websites (URLs) that you want to block in the `website_lists` variable.
- During working hours (configured as 8 AM to 8 PM by default), the script modifies the host file to redirect the specified websites to `127.0.0.1`, effectively blocking access to them.
- During non-working hours, the script restores access to the blocked websites by removing the entries from the host file.

## Configuration

To configure the script for your specific needs, follow these steps:

1. Open the script in a text editor or Python IDE.

2. Modify the `website_lists` variable to include the websites you want to block. For example:

   ```python
   website_lists = ["www.facebook.com", "facebook.com", "es-la.facebook.com"]
   
3. You can adjust the working hours by changing the time range in the following section of the script:
```
if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year,
                                                                    dt.now().month, dt.now().day, 20):
```
By default, it is set to block websites from 8 AM to 8 PM.

4. Save your changes.

## Usage
Clone this repository to your local machine or download the script.

Run the script (e.g., python website_blocker.py) as an administrator or with elevated privileges since it modifies system files.

The script will automatically block the specified websites during the defined working hours and unblock them during non-working hours.

To exit the script, you can press Ctrl + C or close the terminal.

## Notes
Make sure to run the script with administrative privileges to modify the hosts file.

Be cautious when modifying the hosts file, as it can affect the behavior of your computer. Only block websites that you genuinely want to restrict access to.

You can add or remove websites from the website_lists variable to customize the list of blocked websites.

That's it! Use this website blocker script to increase productivity during your working hours by blocking distracting websites.

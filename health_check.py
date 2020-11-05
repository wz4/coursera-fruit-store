#!/usr/bin/env python3

import shutil
import psutil
import time
import socket
import emails

sender = "automation@example.com"
recipient = "student-username"#FIX THIS
subject = 'Upload Completed - Online Fruit Store'
body = 'Please check your system and resolve the issue as soon as possible.'

def system_check():
    #CPU
    cpu = psutil.cpu_percent()
    if cpu > 80:
        subject = 'Error - CPU is over 80%'
        alert(subject)
        return
    #Disk
    total, used, free = shutil.disk_usage("/")
    percent_free = free / total * 100
    if percent_free < 20:
        subject = 'Error - Available disk space is less than 20%'
        alert(subject)
        return
    #RAM
    mem = psutil.virtual_memory()
    available = mem.available / 1000000
    if available < 500:
        subject = 'Error - Available memory is less than 500MB'
        alert(subject)
        return
    #Resolve localhost
    if socket.gethostbyname('localhost') != '127.0.0.1':
        subject = 'Error - localhost cannot be resolved to 127.0.0.1'
        alert(subject)
        return

def alert(subject):
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(message)


if __name__ == "__main__":
    while True:
        system_check()
        time.sleep(60)
#!/usr/bin/env python3

import os
import datetime
import reports
import emails

sender = "automation@example.com"
recipient = "student-username"#FIX THIS
subject = 'Upload Completed - Online Fruit Store'
body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
attachment = '/tmp/processed.pdf'

def process_fruit():
    fruit_dir = 'supplier-data/descriptions/'
    fruits = []
    paragraph = ''
    for file in os.listdir(fruit_dir):
        with open(fruit_dir + file) as f:
            #fruits.append({'name': f[0], 'weight': f[1]})
            fruit = {}
            for i, line in enumerate(f, start=0):
                if i is 0:
                    fruit['name'] = line
                elif i is 1:
                    fruit['weight'] = line
                else:
                    break
            fruits.append(fruit)
    for fruit in fruits:
        paragraph += 'name: ' + fruit['name'] + '<br/>' + 'weight: ' + fruit['weight'] + '<br/> + <br/>'
    return paragraph
    

if __name__ == "__main__":
    paragraph = process_fruit()
    reports.generate_report("/tmp/processed.pdf", "The Fruit Report", paragraph)
    message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(message)

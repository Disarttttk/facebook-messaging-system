import csv
import requests
from .models import Account, Contact


def load_accounts_from_file(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 4:
                Account.objects.create(
                    email=row[0],
                    password=row[1],
                    access_token=row[2],
                    page_id=row[3]
                )
            else:
                print(f"Row in accounts file does not have enough columns: {row}")


def load_contacts_from_file(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                Contact.objects.create(
                    name=row[0],
                    facebook_id=row[1]
                )
            else:
                print(f"Row in contacts file does not have enough columns: {row}")


def send_facebook_message(account, contact, message_content):
    access_token = account.access_token
    recipient_id = contact.facebook_id
    page_id = account.page_id

    url = f"https://graph.facebook.com/v11.0/me/messages?access_token={access_token}"

    payload = {
        'recipient': {
            'id': recipient_id
        },
        'message': {
            'text': message_content
        }
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Message sent to {contact.name} ({recipient_id}) from page {page_id} ({account.email})")
    else:
        print(f"Failed to send message to {contact.name} ({recipient_id}) from {account.email}. Status code: {response.status_code}, Response: {response.text}")

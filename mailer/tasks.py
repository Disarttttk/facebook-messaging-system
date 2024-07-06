import time
from celery import shared_task
from .models import Account, Contact, Message
from .utils import send_facebook_message


@shared_task
def send_messages():
    accounts = list(Account.objects.all())
    contacts = list(Contact.objects.all())
    message = Message.objects.latest('send_time')
    account_index = 0

    for contact in contacts:
        account = accounts[account_index]
        send_facebook_message(account, contact, message.content)
        time.sleep(message.delay)
        account_index = (account_index + 1) % len(accounts)

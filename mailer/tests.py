from django.test import TestCase
from django.utils import timezone
from .models import Account, Contact, Message
from .utils import send_facebook_message, load_accounts_from_file, load_contacts_from_file


class MessagingTests(TestCase):

    def setUp(self):
        self.account = Account.objects.create(email='test@example.com', password='testpass', access_token='test_token', page_id='test_page')
        self.contact = Contact.objects.create(name='Test User', facebook_id='123456789')
        self.message = Message.objects.create(content='Test message', delay=0, send_time=timezone.now())

    def test_send_facebook_message(self):
        output = send_facebook_message(self.account, self.contact, self.message.content)
        expected_output = f"Message sent to {self.contact.name} ({self.contact.facebook_id}) from page {self.account.page_id} ({self.account.email})"
        self.assertEquals(output, expected_output)

    def test_load_accounts_from_file(self):
        file_path = '/path/to/accounts.csv'
        load_accounts_from_file(file_path)
        self.assertTrue(Account.objects.filter(email='test1@example.com').exists())

    def test_load_contacts_from_file(self):
        file_path = '/path/to/contacts.csv'
        load_contacts_from_file(file_path)
        self.assertTrue(Contact.objects.filter(name='Test Contact').exists())


from django.test import TestCase
from .models import Message

class MessageTestCase(TestCase):
    def setUp(self):
        self.message = Message.objects.create(author = 'author@gmail.com,', content = 'Author')
    
    def test_message_is_sent(self):
        message = Message.objects.get(content = 'Author')
        self.assertEqual(message, self.message)
    
    def tearDown(self):
        self.message.delete()

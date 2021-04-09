from django.db import models
from .validators import validate_email, validate_message
    
class Message(models.Model):
    content =   models.CharField(max_length = 100, default = 'Nothing to see...', validators = [validate_message])
    author =    models.CharField(max_length = 30, default = 'Unknown user', validators = [validate_email])
    send_time = models.DateTimeField(auto_now_add = True, null = True)
    
    def __str__(self):
        return self.content

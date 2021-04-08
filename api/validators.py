from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if not re.search(regex, email):
        raise ValidationError(_('%(email)s is not valid mail'), params={'email':email})
    
def validate_message(message):
    regex_empty = '^.{0}$'
    regex_length = '^[A-Za-z0-9-@!?.\/#&+\w\s\']{,100}$'
    if re.search(regex_empty, message):
        raise ValidationError(_('Message can not be empty'))
    elif not re.search(regex_length, message):
        raise ValidationError(_('Message should be less than 100 characters'))
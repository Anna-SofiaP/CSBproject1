from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class SpecialCharacterValidator():
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        characters = "[\!?@%:;\$#]"
        if not any(char in characters for char in password):
            raise ValidationError(_('Include at least %(min_length)d special character in the password.') % {'min_length': self.min_length})
        
    def get_help_text(self):
        return _("Password must contain at least %(min_length)d special character.") % {"min_length": self.min_length}
    

class UpperAndLowerCaseValidator():
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if str(password).isupper():
            raise ValidationError(_('Include at least %(min_length)d lowercase letter in the password.') % {'min_length': self.min_length})
        if str(password).islower():
            raise ValidationError(_('Include at least %(min_length)d uppercase letter in the password.') % {'min_length': self.min_length})
        
    def get_help_text(self):
        return _("Password must contain at least %(min_length)d lowercase letter and %(min_length)d uppercase letter.") % {"min_length": self.min_length}
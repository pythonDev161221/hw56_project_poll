from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible

@deconstructible
class MinValueValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

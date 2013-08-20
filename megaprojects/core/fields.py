import shortuuid

from django.db.models import CharField


# This is the default without the UPPERCASE characters
# See:
# http://github.com/stochastic-technologies/shortuuid/blob/50d7f109e25f03b05c74e4e913ca95dbc4b7e091/shortuuid/main.py#L9
# i.e. '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
SHORTUUID_ALPHABET = '23456789abcdefghijkmnopqrstuvwxyz'


# See: http://github.com/nebstrebor/django-shortuuidfield
class ShortUUIDField(CharField):

    """
    A field which stores a Short UUID value in base57 format. This may also
    have the Boolean attribute 'auto' which will set the value on initial save
    to a new UUID value (calculated using shortuuid's default (uuid4)). Note
    that while all UUIDs are expected to be unique we enforce this with a DB
    constraint.
    """

    def __init__(self, auto=True, *args, **kwargs):
        self.auto = auto

        if auto:
            # Do not let the user edit UUIDs if they are auto-assigned
            kwargs['editable'] = False
            kwargs['blank'] = True
            # If you want to be paranoid, set unique=True in your instantiation
            # of the field

        super(ShortUUIDField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        """
        This is used to ensure that we auto-set values if required.
        See CharField.pre_save
        """

        value = super(ShortUUIDField, self).pre_save(model_instance, add)

        # Assign a new value for this attribute if required
        if self.auto and not value:
            # Use only digits & lowercase letters
            shortuuid.set_alphabet(SHORTUUID_ALPHABET)
            value = unicode(shortuuid.uuid())
            setattr(model_instance, self.attname, value)

        return value

    def formfield(self, **kwargs):
        if self.auto:
            return None

        return super(ShortUUIDField, self).formfield(**kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [r"^core\.fields\.ShortUUIDField"])
except ImportError:
    pass

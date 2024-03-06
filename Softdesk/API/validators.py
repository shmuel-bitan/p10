from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_priority(value):
    valid_priorities = ['LOW', 'MEDIUM', 'HIGH']
    if value not in valid_priorities:
        raise ValidationError(
            _('Invalid priority value. Valid values are: %(valid_priorities)s'),
            code='invalid_priority',
            params={'valid_priorities': ', '.join(valid_priorities)},
        )

def validate_tag(value):
    valid_tags = ['BUG', 'FEATURE', 'TASK']
    if value not in valid_tags:
        raise ValidationError(
            _('Invalid tag value. Valid values are: %(valid_tags)s'),
            code='invalid_tag',
            params={'valid_tags': ', '.join(valid_tags)},
        )

def validate_status(value):
    valid_statuses = ['TODO', 'INPROGRESS', 'FINISHED']
    if value not in valid_statuses:
        raise ValidationError(
            _('Invalid status value. Valid values are: %(valid_statuses)s'),
            code='invalid_status',
            params={'valid_statuses': ', '.join(valid_statuses)},
        )
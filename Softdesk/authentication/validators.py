from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_age(age):
    if age is not None and age < 15:
        raise ValidationError(
            _('L\'utilisateur doit avoir au moins 15 ans.'),
            params={'value': age},
        )

def validate_rgpd_consent(can_be_contacted, can_data_be_shared):
    if can_be_contacted is False and can_data_be_shared is False:
        raise ValidationError(
            _('L\'utilisateur doit accepter au moins une option : Peut être contacté ou Peut partager les données.'),
            params={'can_be_contacted': can_be_contacted, 'can_data_be_shared': can_data_be_shared},
        )
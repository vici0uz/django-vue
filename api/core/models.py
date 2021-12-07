from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel

from crum import get_current_user


# Create your models here.
class BaseModel(TimeStampedModel):
    
    class Meta:
        abstract = True
    
    created = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_created_by', verbose_name=_("User"), on_delete=models.PROTECT)
    modified = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_modified_by',verbose_name=_("User"), on_delete=models.PROTECT)
    active = models.BooleanField(verbose_name=_("Activo"), default=True)
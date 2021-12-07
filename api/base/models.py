from django.db import models
from core.models import BaseModel


# Create your models here.

class Person(BaseModel):
    name = ''
    lastname = ''


class 
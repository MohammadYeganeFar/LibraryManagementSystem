from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    profile = models.ImageField(upload_to='profiles/')

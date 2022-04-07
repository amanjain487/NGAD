import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=100)
    avatar = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    wasMarksUser = models.BooleanField(default=False)
    utmSource = models.CharField(max_length=100)
    utmMedium = models.CharField(max_length=100)
    utmCampaign = models.CharField(max_length=100)
    utmTerm = models.CharField(max_length=100)

    objects = UserManager()


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    def __str__(self):
        return self.title


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=1000, null=False)
    fileURL = models.CharField(max_length=10000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    isRestricted = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)
    # categories = ArrayField(models.ForeignKey(Category, on_delete=models.CASCADE))
    totalDownloads = models.BigIntegerField()
    objects = UserManager()

    def __str__(self):
        return self.fileURL


class DownloadLogs(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    utmSource = models.CharField(max_length=100)
    utmMedium = models.CharField(max_length=100)
    utmCampaign = models.CharField(max_length=100)
    utmTerm = models.CharField(max_length=100)

    objects = UserManager()

    def __str__(self):
        return self.created_at

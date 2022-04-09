from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from pymongo import MongoClient
from .models import *


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        existing_user = CustomUser.objects.filter(email=sociallogin.account.extra_data["email"]).first()
        if not existing_user:
            sociallogin.user.wasMarksUser = False
        return


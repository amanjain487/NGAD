import json

from pymongo import MongoClient
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.dispatch import receiver
from .models import *
from django.http import HttpResponse
from allauth.socialaccount.signals import pre_social_login


@receiver(pre_social_login)
@login_required
def return_file_url(request, **kwargs):
    response_data = {}
    if request.user.is_authenticated:
        response_data["status"] = "success"
        response_data["message"] = "User Logged in Successfully"
    else:
        response_data["status"] = "failure"
        response_data["message"] = "User Authentication Failed"
    return HttpResponse(json.dumps(response_data), content_type="application/json")

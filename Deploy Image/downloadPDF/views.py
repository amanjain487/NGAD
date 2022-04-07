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
        file_id = request.GET.get('file', '')
        if file_id == "":
            response_data['result'] = 'error'
            print(response_data)
            return response_data
        file_requested = File.objects.filter(id=file_id).first()
        print(request.user.id)
        if file_requested:
            download_log = DownloadLogs.objects.create(user=request.user,
                                                       file=file_requested)
            response_data['message'] = file_requested.fileURL
            response_data['result'] = 'success'
            download_log.save()
        else:
            response_data['result'] = 'no file'
        print(response_data)
        return HttpResponse(json.dumps(response_data), content_type="application/json")

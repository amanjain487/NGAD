from django.urls import path
from .views import *

urlpatterns = [
    path('chapter-wise-pdf/', return_file_url),

]

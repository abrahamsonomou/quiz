from django.urls import path
from .views import *

urlpatterns = [
    path(r'',index,name="index"),
    path(r'get_quiz',get_quiz,name="get_quiz"),
]

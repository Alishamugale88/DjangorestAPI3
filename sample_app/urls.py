
from django.contrib import admin
from django.urls import include, path
from .views import StudentView

urlpatterns = [
   path('basic/', StudentView.as_view())    #/api/basic/
]


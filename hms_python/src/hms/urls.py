from django .conf.urls import url
from . import views
from django.urls import path

from .views import(
	index,)

urlpatterns=[
	path(r'',index,name="index")
]
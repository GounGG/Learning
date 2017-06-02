from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'group2/$', views.get_Group)
]

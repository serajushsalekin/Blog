from django.conf.urls import url
from blogapp import views

urlpatterns = [
    url(r'^about/$', views.About.as_view(), name='about'),
]
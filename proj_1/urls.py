from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name="index"),
    url(r'^home/', views.index, name='home'),
    url(r'^success/', views.success, name='success'),

]

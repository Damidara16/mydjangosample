from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.homeView.as_view(), name="index"),
    url(r'^home/', views.index, name='home')
]

from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home),
    url(r'^search$',views.search),
    url(r'^cat/(?P<catid>\d+)',views.getcat)
]

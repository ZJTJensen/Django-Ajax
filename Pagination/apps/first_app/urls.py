from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^all.json$', views.all_json),
    url(r'^all.html$', views.all_html),
    url(r'^find$', views.find),
    url(r'^find_date$', views.date),
    url(r'^create$', views.create),
    url(r'^sum$', views.ranges)
] 
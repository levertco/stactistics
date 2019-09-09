from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$', views.home,name='home'),
    url(r'^website/',views.add_website, name='website'),
    url(r'^review/',views.review,name='review'),
    url(r'sites/',views.my_sites,name='sites')
]


from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', index, name='index'),

]

from django.conf.urls import url, include
from .views import BookList
from .views import fun
from .views import *

urlpatterns = [

    url(r'^$', fun),
    #url(r'^$', BookList.as_view()),
]
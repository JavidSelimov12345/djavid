from django.urls import path
from .views import Homeview,Dview



urlpatterns=[
    path('',Homeview.as_view(),name='home'),
    path('post/<int:pk>/',Dview.as_view(),name='detail')
]
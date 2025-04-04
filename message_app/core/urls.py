from django.urls import path
from . import views

urlpatterns = [
    path('msgs/', views.msg_list, name='msg_list'),
    path('api/msgs/', views.MsgList.as_view(), name='api_msg_list')
]
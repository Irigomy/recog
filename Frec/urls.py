from django.urls import path, include
from Frec import views
from django.conf.urls import url
from . import consumer

urlpatterns = [
    path('', views.login, name='login'),
    path('recog/', views.recog, name='recog'),
    path('attendance/', views.attend, name='attendance'),
    path('student/', views.student, name='student'),
    ]

websocket_urlpatterns = [
  url('ws/recog/', consumer.VideoConsumer.as_asgi()),
]

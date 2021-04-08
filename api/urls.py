from django.urls import path
from . import views

urlpatterns = [
    path('messages/single/', views.messages_single),
    path('messages/single/<int:page>/', views.messages_single),
    path('messages/list/<int:page>/', views.messages_list),
]
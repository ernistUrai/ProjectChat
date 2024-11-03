from django.urls import path
from .views import MessageListView, MessageCreateView

urlpatterns = [
    path('', MessageListView.as_view(), name='chat'),
    path('send/', MessageCreateView.as_view(), name='send_message'),
]
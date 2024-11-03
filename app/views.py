from django.shortcuts import render, redirect
from django.views.generic import ListView,  DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Message
from .forms import MessageForm
# Create your views here.


class MessageListView(ListView):
    model = Message
    template_name = 'chat_list.html'
    context_object_name = 'messages'
    ordering = ['-date']
    

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'chat_create.html'
    success_url = reverse_lazy('chat')  # Билдирүү ийгиликтүү катталгандан кийин кайда өтүү керек
   
    def form_valid(self, form):
       return super().form_valid(form)
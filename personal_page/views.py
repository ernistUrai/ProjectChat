from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import UserRegisterForm
from .models import DirectMessage


# Create your views here.
#Register
def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('user_profile', args=[request.user.id]))
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'{user.username}, your account has been created!')
            login(request, user)
            request.session.set_expiry(16000000)
            return redirect(reverse('user_profile', args=[user.id]))
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})



def login_view(request):
    # Эгер колдонуучу алре кирген болсо, башкы бетке багыттоо
    if request.user.is_authenticated:
        return redirect(reverse('user_profile', args=[request.user.id]))

    # Эгерде бул POST эмес болсо, логин формасын көрсөтүү
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # "Мени эстеп кал" чекити

        # Колдонуучуну аутентификациялоо
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Эстеп калуу үчүн сессиянын мөөнөтүн белгилөө
            if remember_me:
                request.session.set_expiry(16000000)  # 2 жума
            else:
                request.session.set_expiry(0)  # Стандарттык сессия

            messages.success(request, f'Welcome, {username}!')
            return redirect(reverse('user_profile', args=[user.id]))
        else:
            messages.error(request, 'Invalid username or password')

    # Эгерде колдонуучу катталган болсо, логин формасын көрсөтпөөгө болот
    if request.method == 'GET' and 'username' in request.GET:
        username = request.GET['username']
        password = request.GET.get('password')  # Пароль автоматтык түрдө киргизилбейт, бирок бул логикада киргизилиши мүмкүн

        # Колдонуучуну аутентификациялоо
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect(reverse('user_profile', args=[user.id]))
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user/profile.html', {'user': user})

########################################################################




def home(request):
    return render(request, 'home.html')

########################################################################


def send_direct_message(request):
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient_id')
        text = request.POST.get('text')
        recipient = get_object_or_404(User, id=recipient_id)

        # Жаңы билдирүүнү түзүү
        message = DirectMessage(sender=request.user, recipient=recipient, text=text)
        message.save()

        messages.success(request, 'Your message has been sent!')
        return redirect('inbox_view')  # Билдирүүнү жөнөткөндөн кийин келген билдирүүлөрдү көрүү үчүн кайтаруу

    # GET суранычы үчүн форма
    users = User.objects.exclude(id=request.user.id)  # Өзүнөн башка колдонуучуларды алуу
    return render(request, 'send_message.html', {'users': users})


def inbox_view(request):
    received_messages = DirectMessage.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'inbox.html', {'messages': received_messages})


def read_message(request, message_id):
    message = get_object_or_404(DirectMessage, id=message_id, recipient=request.user)
    message.is_read = True
    message.save()
    return redirect('inbox_view')
########################################################################
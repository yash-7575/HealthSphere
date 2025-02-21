from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import User

@login_required
def chat_room(request):
    messages = Message.objects.all()
    users = User.objects.all()  # Get all users for display
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('community')
    else:
        form = MessageForm()
    
    return render(request, 'chat/chat_room.html', {
        'messages': messages,
        'form': form,
        'users': users,  # Pass users to template
    })
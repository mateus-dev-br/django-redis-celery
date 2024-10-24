from django.shortcuts import render, redirect
from .forms import MessageForm
from django.contrib import messages
from .tasks import send_email_task
from .models import EmailTask


def home_view(request):
    form = MessageForm()
    email_tasks = EmailTask.objects.all().order_by('-created_at') 

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            email_task_instance = form.save()
            messages.success(request, 'success')

            send_email_task.delay(email_task_instance.id)

            return redirect('home')
        messages.warning(request, "Erro no formulário!")


    context = {
        'form': form,
        'email_tasks': email_tasks,
    }

    return render(request, 'home.html', context)
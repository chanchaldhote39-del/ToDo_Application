from django.shortcuts import render
from todoApp.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

#backend databse mdhun data geun frontend ver show krel jekhi task apn admin mdhy jaun addd kele ahy te
@login_required
def todo(request): 
    tasks = Task.objects.filter(is_completed=False)
    completed_task = Task.objects.filter(is_completed=True)

    if request.GET.get('search'):
        tasks = tasks.filter(task__icontains=request.GET.get('search'))

    context = {
        'tasks': tasks,
        'completed_task': completed_task,
    }
       
    return render(request, 'todo.html', context)


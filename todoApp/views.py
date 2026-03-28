from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def addTask(request):
    if request.method == "POST":
     task = request.POST.get('task')
    if task:
        Task.objects.create(task=task, user =request.user)
    return redirect('todo')


@login_required
def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed =True
    task.save()
    return redirect('todo')

@login_required
def mark_as_undone(request,pk):
   task = get_object_or_404(Task, pk=pk)
   task.is_completed =False
   task.save()
   return redirect('todo')

@login_required
def delete_undone_task(request,pk):
   task = get_object_or_404(Task, pk=pk)
   task.is_completed =True
   task.delete()
   return redirect('todo')


@login_required     
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo')

@login_required        
def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST": # new task yachyt jail
        new_task = request.POST.get('task') # j# new task yachyt jail
        get_task.task = new_task # ji new task ahy tyla old task sobt match krach
        get_task.save() # new task save
        return redirect('todo') # return toto page
    else:
       context = {
          'get_task' : get_task,
       }
    return render(request,'edit_task.html', context)
            


def register_view(request):
    if request.method == 'POST':
       first_name = request.POST.get('first_name')
       last_name = request.POST.get('last_name')
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = User.objects.filter(username=username)
       

       if user.exists(): # user is exist the return redirec to the register page
          messages.error(request,  "Username Already exist")
          return redirect('register')

       user = User.objects.create(
          first_name = first_name,
          last_name = last_name,
          username = username,
         #  password enscrypt kraycha ahy  tr diect pass tkn tr ithe pass dakvn nahi krn string aste password hume password ko ensycipyrt karke save karna hota hai
       )

       user.set_password(password)
       user.save()
       messages.success(request,  "Account Create Successfully !")
       return redirect('register')

    return render(request,'register.html')








def login_view(request):
    
    if request.method == 'POST':
       username =request.POST.get('username')
       password =request.POST.get('password')

       if not User.objects.filter(username=username).exists():
          messages.error(request,  "Invalid Username")
          return redirect('login')
       
       user = authenticate(username=username, password =password)

       if user is None:
          messages.error(request, 'Invalid pasword')
          return redirect('login')
       
       else:
          login(request,user)
          return redirect('todo')
            
          

    return render(request,'login.html') 




def logout_view(request):
    logout(request)
    return redirect('login')
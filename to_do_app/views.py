from django.shortcuts import render, redirect
from django.contrib import auth


from to_do_app.models import Todo
from to_do_app.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
# def show_todo_all(request):
#     todo_titles = Todo.objects.filter(user=request.user).order_by('-date')
#     context = {
#         'title': 'Todo\'s',
#         'todo_titles': todo_titles
#     }
#     return render(request, 'weather.html', context)

@login_required
def show_todo_active(request):
    todo_titles = Todo.objects.filter(user=request.user, status='active').order_by('-date')
    context = {
        'title': 'Active Todo\'s',
        'quantity': todo_titles.count(),
        'todo_titles': todo_titles
    }
    return render(request, 'index.html', context)

@login_required
def show_todo_completed(request):
    todo_titles = Todo.objects.filter(user=request.user, status='completed').order_by('-date')
    context = {
        'title': 'Completed Todo\'s',
        'quantity': todo_titles.count(),
        'todo_titles': todo_titles
    }
    return render(request, 'index.html', context)

@login_required
def check_todo(request, todo_id, todo_status):
    new_todo_status = 'completed' if todo_status=='active' else 'active'
    Todo.objects.filter(id=todo_id, user=request.user).update(status=new_todo_status)
    return redirect(request.META['HTTP_REFERER'])

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('to_do_app:show_todo_active')
    else:
        form = UserLoginForm()
    context = {
        'title': 'Login',
        'form': form,

    }
    return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('to_do_app:login')
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'signup.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('to_do_app:login')

@login_required
def add_todo(request):

    title = request.POST['new_todo_input']
    obj = Todo.objects.create(title=title, user=request.user)
    obj.save()
    return redirect('to_do_app:show_todo_active')

@login_required
def edit_todo(request, todo_id):
    title = request.POST['edit_todo_input']
    Todo.objects.filter(id=todo_id, user=request.user).update(title=title)
    return redirect(request.META['HTTP_REFERER'])

@login_required
def delete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect(request.META['HTTP_REFERER'])

@login_required
def clear_completed_todos(request):
    Todo.objects.filter(user=request.user, status='completed').delete()
    return redirect(request.META['HTTP_REFERER'])
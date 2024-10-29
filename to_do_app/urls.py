from django.urls import path
from to_do_app.views import show_todo_active, show_todo_completed, login, register, logout, add_todo, delete_todo, edit_todo, check_todo, clear_completed_todos

app_name = 'to_do_app'
urlpatterns = [
    # path('all/', show_todo_all, name='show_todo_all'),
    path('active/', show_todo_active, name='show_todo_active'),
    path('completed/', show_todo_completed, name='show_todo_completed'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('add_todo/', add_todo, name='add_todo'),
    path('check_todo/<int:todo_id>/<str:todo_status>', check_todo, name='check_todo'),
    path('edit_todo/<int:todo_id>', edit_todo, name='edit_todo'),
    path('delete_todo/<int:todo_id>', delete_todo, name='delete_todo'),
    path('clear_completed_todos/', clear_completed_todos, name='clear_completed_todos'),
]
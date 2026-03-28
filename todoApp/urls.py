from . import views
from django.urls import path

urlpatterns =[
 
    path('addTask/',views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),
    path('delete_task/<int:pk>/',views.delete_task, name='delete_task'),
    path('mark_as_undone/<int:pk>/',views.mark_as_undone, name='mark_as_undone'),
    path('delete_undone_task/<int:pk>/',views.delete_undone_task, name='delete_undone_task'),
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),


# aurthentication url
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),




]

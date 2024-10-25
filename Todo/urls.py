from django.urls import path
from .views import todo , Task_Info

urlpatterns=[
    path('todo',todo,name='todo'),
    path('task_info',Task_Info,name='task_info')
]
from django.urls import path
from .views import todo , Task_Info  , edit , search


app_name='Todo'

urlpatterns=[
    path('todo',todo,name='todo'),
    path('task_info',Task_Info,name='task_info'),
    path('edit',edit,name="edit"),
]
from django.urls import path
<<<<<<< HEAD
from .views import todo , Task_Info  , edit , search


app_name='Todo'
=======
from .views import todo , Task_Info  , edit , search 
>>>>>>> b71e10d733e15a6c7cf2820404b1e576904304e3

urlpatterns=[
    path('todo',todo,name='todo'),
    path('task_info',Task_Info,name='task_info'),
    path('edit',edit,name="edit"),
<<<<<<< HEAD
=======
    path('search',search,name="search"),
>>>>>>> b71e10d733e15a6c7cf2820404b1e576904304e3
]
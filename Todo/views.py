from django.shortcuts import render, redirect ,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Todo_list

@login_required
def todo(request):
    if request.method == "POST":
       title = request.POST.get('taskTitle')
       description = request.POST.get('taskDescription')
       date = request.POST.get('taskDate')
       completed_task_id = request.POST.get('completed_task_id') # get the completed task id 
       completed_status = request.POST.get('completed')  # Get the status of the checkbox
       delete_task_id = request.POST.get('delete_task_id') # get the id of the task the user want to delete



    # Check if a new task is being added
       if title:
            Todo_list.objects.create(user=request.user,Title=title , Description=description , Date=date)  # Create a new task

       if completed_task_id:
         try:
            task = Todo_list.objects.get(id=completed_task_id, user=request.user)  # Retrieve the task
            # Update the task's completion status based on the checkbox value
            if completed_status == "True":
                task.completed = True
            else:
                task.completed = False
            task.save()  # Save the changes
         except Todo_list.DoesNotExist:
                return HttpResponse('Task not found.', status=404)
                   
       if delete_task_id: # ensure there is id
            try:           
                delete_item=Todo_list.objects.get(id=delete_task_id,user=request.user)# retrieve the task the user want to delete
                delete_item.delete() # delete the task

            except Todo_list.DoesNotExist: # handle Error
                return HttpResponse('Task not found.', status=404)
            
    tasks = Todo_list.objects.filter(user=request.user)  # Retrieve all tasks (both completed and incomplete)
    return render(request, 'todo/todo.html', {'tasks': tasks})  # Pass all tasks to the template


def Task_Info(request):
    if request.method == "POST":
        info_task_id = request.POST.get('Info_task_id')

        if info_task_id:
            info=Todo_list.objects.get(id=info_task_id,user=request.user)
            
    tasks = Todo_list.objects.filter(user=request.user)  # Retrieve all tasks (both completed and incomplete)
    return render(request,"todo/show_info.html",{"info":info , "tasks":tasks})       

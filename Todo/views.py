from django.shortcuts import render, redirect ,HttpResponse , HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from .models import Todo_list


@login_required # just the user logged in can access this view
def todo(request):
    if request.method == "POST": # if the form is submitted
       title = request.POST.get('taskTitle') # get the title of the task
       description = request.POST.get('taskDescription') # get the description of the task
       date = request.POST.get('taskDate') # get the date of the task
       completed_task_id = request.POST.get('completed_task_id') # get the completed task id 
       completed_status = request.POST.get('completed')  #  Get the status of the checkbox
       delete_task_id = request.POST.get('delete_task_id') # get the id of the task the user want to delete

       #  Check if a new task is being added
       if title:
            Todo_list.objects.create(user=request.user,Title=title , Description=description , Date=date)  # Create a new task

       if completed_task_id: # if the user has checked a task as completed
         try:
            task = Todo_list.objects.get(id=completed_task_id, user=request.user)  # Retrieve the task
            # Update the task's completion status based on the checkbox value
            if completed_status == "True":# if the checkbox is checked
                task.completed = True # mark the task as completed
            else: # if the checkbox is unchecked
                task.completed = False # mark the task as not completed
            task.save()  # Save the changes

         except Todo_list.DoesNotExist: # if the task does not exist
                return HttpResponse('Task not found.', status=404) # return a 404 error
         
       if delete_task_id: # ensure there is id
            try: 
                delete_item=Todo_list.objects.get(id=delete_task_id,user=request.user)# retrieve the task the user want to delete
                delete_item.delete() # delete the task

            except Todo_list.DoesNotExist: # handle Error
                return HttpResponse('Task not found.', status=404) # return a 404 error

        
    tasks = Todo_list.objects.filter(user=request.user)  #Retrieve all tasks (both completed and incomplete)
    return render(request, 'todo/todo.html', {'tasks': tasks})  #  Render the todo.html template with the tasks

@login_required # just the user logged in can access this view
def Task_Info(request): 
    info=None # intialize value for this variable
    # check if the method is POST
    if request.method == "POST": 
        info_task_id = request.POST.get('Info_task_id') # bring the id of the task the user want to know info about it

        if info_task_id: # if there is id
            info=Todo_list.objects.get(id=info_task_id,user=request.user) # get the element by id and the logged in user
            
    tasks = Todo_list.objects.filter(user=request.user)  # Retrieve all tasks (both completed and incomplete)
    return render(request,"todo/show_info.html",{"info":info , "tasks":tasks})   # render the the show info page , and create context

@login_required # just the user logged in can access this view
def edit(request):
    edit_task = None # initialize variable
    if request.method == "POST": # check if the method is POST
        edit_task_id = request.POST.get("edit_task_id") # bring the id of the task the user want to edit

        if edit_task_id:# if there is id
            try:  # Try to retrieve the task

                edit_task = Todo_list.objects.get(id=edit_task_id, user=request.user) # Retrieve the task

                title = request.POST.get('title')  # Get the new title from the form
                date = request.POST.get('date') # Get the new date from the form
                description = request.POST.get('description') # Get the new description from the form

                if title: # if there is title
                    edit_task.Title = title # update the title of the task
                if date: # if there is date
                    edit_task.Date = date # update the date of the task
                if description: # if there is description
                    edit_task.Description = description # update the description of the task
                edit_task.save()  # Save changes
                
            except Todo_list.DoesNotExist:# handle Error
                return HttpResponse("Task not found.",status=404) # return error message if task not found

    tasks = Todo_list.objects.filter(user=request.user) # Retrieve all tasks (both completed and incomplete)
    return render(request, "todo/edit.html", {"edit_task": [edit_task], "tasks": tasks}) # render the edit page and create context

@login_required
def search(request):
    info = None
    search_text = request.GET.get('search_text', '').strip()  # Get the search query and strip whitespace
    
    print(f"Search Text: '{search_text}'")  # Debugging: print the search text
    
    if search_text:  # Check if search_text is not empty
        info = Todo_list.objects.filter(user=request.user, Title=search_text)  # Use icontains for case-insensitive search
        print(f"Tasks Found: {info}")  # Debugging: print the tasks found
    else:
        info = Todo_list.objects.filter(user=request.user)  # Optionally return all tasks if search_text is empty
        print("No search text provided, returning all tasks.")
    
    return render(request, "todo/search_results.html", {"info": info})
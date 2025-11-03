from uuid import uuid4

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse


task_list = []

def get_task_list_view(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='list.html', context={'tasks': task_list})


def add_task_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request=request, template_name='add.html')
    elif request.method == 'POST':
        form = request.POST

        title = form.get('title')
        description = form.get('description')
        priority = form.get('priority')
        status = form.get('status')
        deadline = form.get('deadline')

        # validation
        if title == '':
            return HttpResponse("Titleni unitdingiz.", status=400)
        elif priority not in ['low', 'medium', 'high']:
            return HttpResponse("priorityni unitdingiz.", status=400)
        elif status not in ['todo', 'inprogress', 'done']:
            return HttpResponse("statusni unitdingiz.", status=400)
        elif deadline == '':
            return HttpResponse("deadlineni unitdingiz.", status=400)
        else:
            new_task = {
                'id': str(uuid4()),
                'title': title,
                'description': description,
                'priority': priority,
                'status': status,
                'deadline': deadline,
            }
            task_list.append(new_task)

            return redirect(reverse('todos:list'))
    

def task_detail_view(request: HttpRequest, task_id: str) -> HttpResponse:
    for task in task_list:
        if task['id'] == task_id:
            return render(request=request, template_name='detail.html', context={'task': task})
    return redirect(reverse('todos:list'))

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# Create your views here.

from tasks.models import Task


def index(request):
    tasks = Task.objects.all()

    SIZE = len(tasks)

    paginator = Paginator(tasks, 8)

    # return render(request, 'index.html', {'tasks': tasks, 'size': SIZE})
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"page_obj": page_obj, "tasks": tasks})


def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        # Create a new task object and save it to the database
        Task.objects.create(title=title, description=description)
        # Redirect to a success page or render another template
        return redirect('/tasks')
    else:
        return render(request, 'new/create.html')

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# Create your views here.

from tasks.models import Task
import time


def format_time(elapsed):
    if elapsed < 1:
        return "{:.2f} ms".format(elapsed * 1000)  # Convert seconds to milliseconds
    else:
        return "{:.2f} sec".format(elapsed)


def index(request):
    start_time = time.time()
    tasks = Task.objects.all()

    paginator = Paginator(tasks, 8)

    # Count the total number of tasks
    total_tasks_count = tasks.count()

    # Render the template with the necessary context
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    end_time = time.time()
    elapsed_time = end_time - start_time
    formatted_time = format_time(elapsed_time)
    return render(request, "index.html", {"page_obj": page_obj, "tasks": tasks, "elapsed_time": formatted_time,
                                          "total_tasks_count": total_tasks_count})

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

# Create your views here.
import time

from django.shortcuts import render

from tasks import models
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from tasks.models import Task


def format_time(elapsed):
    if elapsed < 1:
        return "{:.2f} ms".format(elapsed * 1000)  # Convert seconds to milliseconds
    else:
        return "{:.2f} sec".format(elapsed)


def userIndex(request):
    start_time = time.time()
    tasks = models.Task.objects.values('id', 'title', 'description')
    # tasks = Task.objects.values('title', 'description', 'created_at')  # Fetch all tasks from the database

    paginator = Paginator(tasks, 10)  # Paginate tasks, with 8 tasks per page
    page_number = request.GET.get('page')  # Get current page number from URL parameter
    user = request.user
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        page_obj = paginator.get_page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        page_obj = paginator.page(paginator.num_pages)

    end_time = time.time()
    elapsed_time = end_time - start_time
    formatted_time = format_time(elapsed_time)
    return render(request, 'profile.html', {'user': user, "page_obj": page_obj, "formatted_time": formatted_time})

# def profile_view(request):
#     start_time = time.time()
#     tasks = models.Task.objects.all()
#
#     paginator = Paginator(tasks, 8)  # Paginate tasks, with 8 tasks per page
#     page_number = request.GET.get('page')  # Get current page number from URL parameter
#
#     page_obj = paginator.get_page(page_number)  # Get the current page object
#
#     user = request.user
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     formatted_time = format_time(elapsed_time)
#     return render(request, 'profile.html', {'user': user, "page_obj": page_obj, "formatted_time": formatted_time})

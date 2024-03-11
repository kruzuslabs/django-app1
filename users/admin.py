from django.contrib import admin

# Register your models here.

from tasks import models

admin.site.register(models.Task)
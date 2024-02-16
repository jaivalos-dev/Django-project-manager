from django.contrib import admin
from .models import project, Task

admin.site.register(project)
admin.site.register(Task)
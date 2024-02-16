from django.http import HttpResponse, JsonResponse
from .models import project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

def index(request):
    title = "Django Course"
    return render(request, "index.html", {
        'title': title
    })

def about(request):
    return render(request, "about.html")

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" %username)

def projects(request):
    projects = project.objects.all()
    return render(request, "projects/projects.html", {
        "projects": projects
    })

def create_project(request):
    if request.method == 'GET':
        return render(request, "projects/create_project.html", {
            "form": CreateNewProject()
        })
    else: 
        project.objects.create(name=request.POST['name'])
        return redirect("/projects/")

def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html",{
        "tasks": tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, "tasks/create_task.html", {
            "form": CreateNewTask()
        })
    else: 
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect("/tasks/")
    
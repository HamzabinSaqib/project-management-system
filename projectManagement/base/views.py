from django.shortcuts import render

projects = [
    {'id': 1, 'name':'Project 1'},
    {'id': 2, 'name':'Project 2'},
    {'id': 3, 'name':'Project 3'},
    {'id': 4, 'name':'Project 4'}
]

def login(req):
    return render(req, 'base/login.html')

def home(req):
    context = {'projects':projects}
    return render(req, 'base/home.html', context)

def project(req, pk):
    project = None
    for i in projects:
        if i['id'] == int(pk):
            project = i
    context = {'project': project}
    return render(req, 'base/project.html', context)
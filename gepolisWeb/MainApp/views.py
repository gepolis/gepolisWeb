from django.shortcuts import render

def home(request):
    return render(request,"pages/home.html")

def order(request):
    return render(request,"pages/order.html")

def info(request):
    return render(request,"pages/info.html")

def about(request):
    return render(request,"pages/about.html")

def projects(request):
    return render(request,"pages/projects.html")

def dashboard(request):
    return render(request,"pages/dashboard/index.html")
def dashboard_messages(request):
    return render(request,"pages/dashboard/messages.html")
def dashboard_chat(request,id):
    return render(request,"pages/dashboard/chat.html")

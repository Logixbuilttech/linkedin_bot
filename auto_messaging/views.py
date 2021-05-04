from django.shortcuts import render
from django.http import HttpResponse
from send_message import views
from .forms import Choice,FileUpload,Text_input
import csv

api = views.get_api_obj()
uname_list = []

def form_input(request):
    form = Choice(request.POST)
    if form.is_valid():
        selected = form.cleaned_data.get("csv_upload")
    return render(request, 'uname_fetch.html',{'file': selected})

def uname_input_choice(request):
    return render(request, "choice.html")

def csv_file(request):
    form = FileUpload(request.POST)
    if form.is_valid():
        file_name=str(request.FILES['csv_file'])
        if check_file_type(file_name):
            handle_uploaded_file(request.FILES['csv_file'])
            return HttpResponse("Done")
        else:
            return HttpResponse("Only CSV Files Supported in the format of 'file_name.csv'")
    else:
        return HttpResponse("Error")

def uname_send(request):
    global uname_list
    form = Text_input(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        uname_list = str.split(username,",")
        print(uname_list)
        return HttpResponse("Done")
    else:
        return HttpResponse("Error")

def handle_uploaded_file(f):
    with open('temp/upload.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    csv_to_list()

def check_file_type(file):
    if str.split(file,".")[1] == 'csv':
        return True
    else:
        return False

def csv_to_list():
    global uname_list
    with open("temp/upload.csv",newline='') as f:
        for line in f.readlines():
            l,name = line.strip().split(',')
            uname_list.append((l,name))
    print(uname_list)

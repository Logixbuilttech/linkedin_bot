from django.shortcuts import render
from django.http import HttpResponse
from send_message import views
from .forms import Choice,FileUpload,Text_input

api = views.get_api_obj()

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
        csv_file = request.FILES['csv_file']
        return HttpResponse("Done")
    else:
        return HttpResponse("Error")

def uname_send(request):
    form = Text_input(request.POST)
    if form.is_valid():
        uname = request.FILES['uname']
        print(uname)
        return HttpResponse("Done")
    else:
        return HttpResponse("Error")
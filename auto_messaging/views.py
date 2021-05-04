from django.shortcuts import render
from django.http import HttpResponse
#from send_message import views
from .forms import Choice


#api = views.get_api_obj()

def form_input(request):
    form = Choice(request.POST)
    selected = "Not Found"
    print(form)
    if form.is_valid():
        selected = form.cleaned_data.get("input")
        print(selected)
    return HttpResponse(selected)

def uname_input_choice(request):
    return render(request, "choice.html")


# Create your views here.
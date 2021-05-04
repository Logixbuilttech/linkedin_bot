"""linkedin_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from send_message import views as sending
from auto_messaging import views as auto_sending

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', sending.index),
    path('send_message/', sending.send_message),
    path('linkedin_login_form/', sending.linkedin_login_form),
    path('linkedin_login/', sending.linkedin_login),
    path('', sending.dashboard),
    path('logout_linkedin/', sending.logout_linkedin),
    path('render_choice/', auto_sending.form_input),
    path('input_choices/', auto_sending.uname_input_choice),

]

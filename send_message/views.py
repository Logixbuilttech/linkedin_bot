from django.shortcuts import render
from django.http import HttpResponse
from linkedin_api import Linkedin
from .forms import NameForm,CredsForm
from django.shortcuts import redirect
import ctypes

api = None
api_id = None              

def dashboard(request):
	global api_id
	if api_id != None:
		fname,lname = get_name(request) # If session exist then dashboard will have Name of Users
	else:
		return render(request,'dashboard.html',{'fname':'Welcome','lname':'Guest','flag':'True'}) # Else dashboard will have text 
	return render(request,'dashboard.html',{'fname':fname,'lname':lname,'flag':'False'})

def index(request):
	# Checking for session
	global api_id
	if api_id != None:
		return render(request,'index.html') # If session exists, Message Sending form will open
	else:
		return redirect('/linkedin_login_form') # Else wil be redirected to login page

def linkedin_login_form(request): # Route for Login Form
	return render(request,'linkedin_login.html')

def linkedin_login(request):
	# Form response render and linkedin logging in.
	form = CredsForm(request.POST)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
	global api # Using Global object for accessing this object in other functions
	api = Linkedin(username,password) # Logging in using the clients credentials
	global api_id
	api_id = id(api) # Creating session
	return redirect('/index')

def send_message(request):
	# Form response for sending message
	form = NameForm(request.POST)
	if form.is_valid():
		profile_user_id = form.cleaned_data['profile_user_id']
		message_body = form.cleaned_data['message_body']
		global api_id # Using api object from session
		sending_message(profile_user_id,message_body,api_id)
	else :
		return HttpResponse("Form Invalid")

	return HttpResponse("The Message "+message_body+" was sent to user with user id "+profile_user_id)

def sending_message(profile_user_id,message_body,api_id):
	# This function will be used for sending message to client's user.
	# Converting id of object to object
	api = ctypes.cast(api_id, ctypes.py_object).value
	print(type(api))
	# Fetching recipirnts complete profile
	recipient_profile = api.get_profile(profile_user_id)
	# Checking if the client is already connected to user or not.
	
	try:
	# If user already in connection fetching conversation urn and sending message
		api.get_conversation_details(recipient_profile['profile_id']) 
		conversation_details = api.get_conversation_details(recipient_profile['profile_id'])
		conversation_urn_id = conversation_details['backendUrn'].split(':')[-1]
		api.send_message(message_body=message_body,conversation_urn_id=conversation_urn_id)
	except:
	# Else sending invitation with the same message
  		api.add_connection(profile_public_id=profile_user_id,message=message_body,profile_urn=recipient_profile['profile_id'])

def logout_linkedin(request):
	# For Clearing cookies
	global api_id
	api_id = None
	return redirect('/linkedin_login_form/')

def get_name(request):
	# Function is used to fetch client's firstname and lastname
	global api_id
	api = ctypes.cast(api_id, ctypes.py_object).value
	my_profile = api.get_user_profile()
	first_name = my_profile['miniProfile']['firstName']
	last_name = my_profile['miniProfile']['lastName']

	return (first_name,last_name)

def get_api_obj():
	# For sending the api object to other functions
	global api_id
	if api_id == None:
		return None
	else:
		api = ctypes.cast(api_id, ctypes.py_object).value
		return api
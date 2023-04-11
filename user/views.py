from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  


def register_request(request):

	if request.method == 'POST':
		form = NewUserForm(request.POST)  
		if form.is_valid():  
            # save form in the memory not in database
			user = form.save(commit=False)  
			user.is_active = False  
			user.save()
            # to get the domain of the current site 
			current_site = get_current_site(request)
			mail_subject = 'Mandarin Flash registration activation link'
			message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),  
            })
			print("message: ", message)
			print("message type: ", type(message))
			to_email = form.cleaned_data.get('email')
			print("to email: ", to_email)
			print("to email type: ", type(to_email))
			email = EmailMessage(mail_subject, message, to=[to_email])
			print("Email :", email)
			email.send()
			return HttpResponse(f'We just sent an email to { to_email }. Click the activation link in the email to confirm your signup.')
	else:
		form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")


def activate(request, uidb64, token):
	try:  
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None 
	
	if user is not None and account_activation_token.check_token(user, token):  
		user.is_active = True  
		user.save()
		
		return redirect("login")
	else:
		return HttpResponse('Activation link is invalid!')

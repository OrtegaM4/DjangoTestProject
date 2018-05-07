from django.shortcuts import render
from test_app.models import UserProfileInfo #Webpage,AccessRecord,Topic
from test_app.forms import UserForm,UserProfileInfoForm

#Additional Imports:
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #context_dict = {'text':'hello world','number':100}
    return render(request,'test_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user= user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            if 'profile_pic' in request.FILES:
                print('Found your photo')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request, 'test_app/registration.html',{'user_form':user_form,
                                                     'profile_form':profile_form,
                                                       'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active!")
        else:
            print("Someone attempted to login and failed")
            print("Username: {} and password {} ".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'test_app/login.html')









#First Form View Created, Returns Data Entered.
# def form_name_view(request):
#     form = forms.FormName()
#     if request.method == 'POST':
#         form = forms.FormName(request.POST)
#
#         if form.is_valid():
#             #DO SOMETHING CODE
#             print("Form is Valid Congrats.")
#             print("NAME:"+form.cleaned_data['name'])
#             print("EMAIL:"+form.cleaned_data['email'])
#             print("TEXT:"+form.cleaned_data['text'])
#
#
#
#
#             return render(request, 'test_app/form_page.html',{'form':form} )

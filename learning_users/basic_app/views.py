from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

#for using django LOGIN support
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    print('222 {}'.format(request.method))
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False

    if request.method =='POST':
        print('111 {}'.format(request.POST))
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            #converts clear text password to SHA1 to be stored in db
            #uses one of the password hashers specified in settings.py(Ex:Argon2)
            user.set_password(user.password)
            user.save()

            #save the form only but do not commit to db
            profile = profile_form.save(commit=False)
            #update the user first since this has 1-1 relationship
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES['profile_pics']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(
        request,
        'basic_app/registration.html',
        context={
            'registered': registered,
            'user_form': user_form,
            'profile_form':profile_form
        }
    )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User {} is not active".format(username))
        else:
            print("{} tried to login and failed".format(username))
            return HttpResponse("Invalid login creds supplied for User {}".format(username))
    else:
        return render(request, 'basic_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

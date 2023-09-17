from django.shortcuts import render,redirect
from .forms import UserCreationForm, UserUpdateForm
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(request,f' Welcome {new_user} to our Website')
            return redirect('login')

    else:
        form=UserCreationForm()

    return render(request, 'user/register.html',{
        'title':'Register',
        'form':form,
    })

@login_required(login_url='login')
def profile(request):
    posts= Post.objects.filter(author = request.user)
    return render(request, 'user/profile.html',{
        'title':'Profile',
        'posts':posts
    })


def profile_update(request):
    if request.method =='POST':
       user_form= UserUpdateForm(request.POST, instance=request.user)
      
       
       if user_form.is_valid :
           user_form.save()
         
           messages.success(request,f' Update is Done')
           return redirect('profile')

     
    else:
        user_form= UserUpdateForm(instance=request.user)
        

    context={
        'title':'Profile_Update',
        'user_form':user_form,
        
        
          
    }

    return render(request, 'user/profile_update.html',context)
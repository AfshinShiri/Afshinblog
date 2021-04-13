
from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url="/accounts/login")
def comments(request):

    if request.method == "POST":
        form = forms.commentsform(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('homepage')
    else:
        form = forms.commentsform()
    return render(request,'comments/comments.html',{'form':form})

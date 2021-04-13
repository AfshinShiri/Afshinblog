from django.shortcuts import render, HttpResponse
from comments import forms
from comments import models
from comments import urls



def home(request):
    comments = models.comments.objects.all().order_by('-date')
    args = {'comments':comments}
    return render(request,'home.html',args)
    # return HttpResponse('home')



def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

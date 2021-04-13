from django.shortcuts import render,HttpResponse

# Create your views here.
def gallery_list(request):
    return render(request,'gallery/gallery.html')

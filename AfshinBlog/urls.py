
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from articles.views import article_list



app_name='AfshinBlog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.home,name='homepage'),
    path('gallery/',include('gallery.urls')),
    path('comments/',include('comments.urls')),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

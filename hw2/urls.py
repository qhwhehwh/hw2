
from django.contrib import admin
from django.urls import path, include
import blogapp.views
import account.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home,name="home"),
    path('blog/',include('blogapp.urls')),
    path('accout/',include('account.urls')),
    path('portfo/',portfolio.views.portfo,name="portfo"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

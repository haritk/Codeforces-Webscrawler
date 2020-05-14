
from django.contrib import admin
from django.urls import path,include
from mysite.core import views
#https://docs.djangoproject.com/en/2.1/topics/auth/default/#module-django.contrib.auth.forms
#this contains accounts waala path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name= "signup"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('secret/',views.secret,name="secret"),
    path('',views.home,name ="home"),
]

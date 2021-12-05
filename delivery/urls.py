
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    
    path('sign-in/',auth_views.LoginView.as_view(template_name="sign-in.html")),
    path('sign-out/',auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/', views.sign_up),



    path('customer/', views.customer),
    path('courier/', views.courier),
    path('', include('social_django.urls', namespace='social')),
]   

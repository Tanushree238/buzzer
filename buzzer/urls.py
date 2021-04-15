"""buzzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('home_page/', views.home_page, name = 'home'),
    path('admin_page/', views.admin_page, name = 'admin'),
    path('admin_page/<int:ques_id>', views.admin_page, name = 'admin1'),
    path('buzzer_start/<int:ques_no>', views.buzzer_start, name = 'buzzer_start'),
    path('buzzer_end/<int:ques_no>', views.buzzer_end, name = 'buzzer_end'),
    path('press_buzzer/<str:name>', views.press_buzzer, name = 'press_buzzer'),
] 
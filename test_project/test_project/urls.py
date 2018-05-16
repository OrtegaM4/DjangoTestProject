"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from test_app.views import IndexView
from test_app import views
from django.urls import path



urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    url(r'^admin/', admin.site.urls),
    url(r'test_app/',include('test_app.urls')),
    #url(r'^formpage/',views.form_name_view, name='form_name'),
    #url(r'^users/',views.users,name='users'),
    url(r'^logout/$',views.user_logout, name='logout')

]

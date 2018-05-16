from django.conf.urls import url
from test_app import views
from django.urls import include, path
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView, RedirectView
from test_app.views import IndexView, SchoolListView, SchoolDetailView, SchoolUpdateView


#TEMPLATE TAGGING
app_name = 'test_app'


urlpatterns= [
    url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
    url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
    path('',views.SchoolListView.as_view(),name='list'),
    path('create/',views.SchoolCreateView.as_view(), name='create'),
    path('register/',views.register,name='register'),
    url('^user_login/',views.user_login, name='user_login'),
    ]

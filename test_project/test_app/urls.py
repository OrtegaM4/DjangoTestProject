from django.conf.urls import url
from test_app import views

#TEMPLATE TAGGING
app_name = 'test_app'


urlpatterns= [
    url(r'^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    #url(r'^relative/$',views.relative,name='relative'),
    url(r'^user_login/$',views.user_login, name='user_login'),
]

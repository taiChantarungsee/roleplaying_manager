from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from blog.views import *

urlpatterns = [ # using the template {{ url 'url_name'}} we can refer to the URL in the template without hard coding it, e.g. for a link. 
    #url(r'^$', TemplateView.as_view(template_name='blog/main.html')),

    #URLs for character builder
    #url(r'^dnd/$', char_builder, name='char_builder'),
    url(r'^character/$', char_builder, name='char_builder'),
    url(r'^new_user/$', CreateUser.as_view(), name='create_user'),
    url(r'^login/$', auth_views.login, {'template_name':'blog/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'blog/logout.html'}, name='logout'),
    url(r'^character/detail/(?P<pk>\d+)/$', character_detail, name='character_detail'),    

]

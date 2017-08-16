from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [ # using the template {{ url 'url_name'}} we can refer to the URL in the template without hard coding it, e.g. for a link. 
    url(r'^$', TemplateView.as_view(template_name='blog/main.html')),
    url(r'^list/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),

    #URLs for character builder
    #url(r'^dnd/$', views.char_builder, name='char_builder'),
    url(r'^character/$', views.char_builder, name='char_builder'),

    #URLs for polling
    # ex: /polls/
    url(r'^$/polls', views.IndexView.as_view(), name='index'), # Combine this (and relevant views with 'post_list'?)
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    #basic_app:list is referred by basic_app_base.html
    url(r'^$', views.SchoolListView.as_view(), name='list'),
    #below regular expression says to take the basic_app domain extension page
    #and use the <pk> primary key and take that as school's detail view
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
]

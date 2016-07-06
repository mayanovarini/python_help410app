from django.conf.urls import url
from help410 import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^chores/(?P<id>[0-9]+)/$', views.gig_detail, name='gig_detail'),
    url(r'^my_chores/$', views.my_gigs, name='my_gigs'),
    url(r'^post_chore/$', views.create_gig, name='create_gig'),
    url(r'^edit_chore/(?P<id>[0-9]+)/$', views.edit_gig, name='edit_gig'),
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^checkout/$', views.create_purchase, name='create_purchase'),
    url(r'^my_purchase/$', views.my_purchase, name='my_purchase'),
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^category/(?P<link>[\w|-]+)/$', views.category, name='category'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about/$', views.about, name='about'),


]

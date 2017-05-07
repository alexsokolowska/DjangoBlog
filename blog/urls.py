from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #beginning^ followed by end $ will match (empty)
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
#post_list is the name of the Unified Resource Locator that will be used to identify the view

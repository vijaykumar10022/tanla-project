from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from MessageRouting import views
# from django.urls import path
urlpatterns = [
		url(r'^gateway/$', views.create, name='index'),
		url(r'^gateway/(\d+)/$',views.data),
		url(r'^route/$',views.myroute),
		url(r'^route/(\d+)/$',views.routedata),
		url(r'^search/route/(?P<number>\d+)/$',views.search),
]
urlpatterns = format_suffix_patterns(urlpatterns)

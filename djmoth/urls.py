from django.urls import include, re_path
from moth.views import RouterView, about, home


urlpatterns = [
    re_path(r'^about/', about, name='about'),
    re_path(r'^$', home, name='home'),
    
    # Send all requests that don't match the previous to the router!
    re_path(r'', RouterView()),
]

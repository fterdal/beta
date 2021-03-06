from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/?', admin.site.urls),
    url(r'^accounts/?', include('allauth.urls')),
    url(r'^accounts/profile/?', include('userprofile.urls', namespace='userprofile')),
    url(r'^offerings/?', include('offering.urls', namespace='offerings')),
]

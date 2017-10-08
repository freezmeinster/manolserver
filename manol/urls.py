from django.conf.urls import url, include
from django.contrib import admin
from deploy.views import landing

urlpatterns = [
    url(r'^$', landing.home, name='home'),
    url(r'^deploy/', include("deploy.urls")),
    url(r'^admin/', admin.site.urls),
]

from django.conf.urls import url
from deploy.views import deploy_api

urlpatterns = [
    url(r'^(?P<code>[\w-]+)/(?P<key>[\w-]+)$', deploy_api.deploy, name='deploy-api-deploy'),
]
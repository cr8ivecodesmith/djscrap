from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns as fsp

from .views import JobListApi, JobUpdateApi


api_urls = fsp([
    url('^jobs$', JobListApi.as_view()),
    url('^jobs/(?P<spider__id>[\d]+)/(?P<name>[\w]+)$',
        JobUpdateApi.as_view()),
])

urlpatterns = [
    url(r'^api/', include(api_urls)),
]

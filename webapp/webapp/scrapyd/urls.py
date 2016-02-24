from django.conf.urls import url, include


api_urls = [
]

urlpatterns = [
    url(r'^api/', include(api_urls)),
]

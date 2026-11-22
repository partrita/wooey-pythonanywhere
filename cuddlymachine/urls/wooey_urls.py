from django.urls import include, path

from .django_urls import *

urlpatterns += [
    #path('admin/', admin.site.urls),
    path('', include('wooey.urls')),
]

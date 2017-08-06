from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import marvel.views

urlpatterns = [
    url(r'^$', marvel.views.index, name='index'),
    url(r'^db', marvel.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]

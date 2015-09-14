from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'feedback.views.home', name='home'),
    url(r'^feedback/', include('feedback.urls', namespace="feedback")),
    url(r'^getmail/', 'feedback.views.getmail', name='getmail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^instructions/$', 'feedback.views.instruction', name='instruction'),
    url(r'^analytics/(?P<br>[A-Za-z]{2})/$', 'feedback.views.analytics'),
    url(r'^login/$', 'feedback.views.login_user', name='login_user'),
    url(r'^analytics/$', 'feedback.views.depart', name='department'),
    url(r'^logout/$', 'feedback.views.logout_user', name='logout_user'),
    url(r'^credits/$', 'feedback.views.credits', name='credits'),
    )


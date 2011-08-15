from django.conf.urls.defaults import *
from KalanTickets.urls import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^Tickets/', include('Kalan.KalanTickets.urls')),   
    (r'^accounts/login/$', login, {'template_name': 'login.html'}),
    (r'^accounts/logout/$', logout_view),                    
    (r'^$', main),
    # Example:
    # (r'^Kalan/', include('Kalan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.defaults import *
from views import *
from django.contrib.auth.views import login

urlpatterns = patterns('',
    (r'^$', dashboard),
    (r'^id/(\d+)', ticket),
    (r'^search/((?:\w+_??)+)', search),
    (r'^create/', createTicket),
    (r'^createnewticket/', createTicket),
    (r'^addentry/(\d+)', addEntry),
    (r'^tag/((?:\w|\s|[&#.!?])+)/', tagView),
    (r'^accounts/login/$', login, {'template_name': 'login.html'}),

    #(r'^loginsuccess/$', loginSuccessRedirect),
)
from django.contrib import admin
from Kalan.KalanTickets.models import *

admin.site.register(Ticket)
admin.site.register(Account)
admin.site.register(Entry)
admin.site.register(Tag)
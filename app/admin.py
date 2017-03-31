from django.contrib import admin
from app.models import Ticket
# Register your models here.


def make_published(modeladmin, request, queryset):
    queryset.update(approved=True)
make_published.short_description = "Mark selected ticktes as not fake"

class TicketAdmin(admin.ModelAdmin):
	actions = [make_published]


admin.site.register(Ticket, TicketAdmin)
from django.contrib import admin
from mzm_api.models import Root, Occurrence, Taxon, Location, Event, Identification

admin.site.register(Root)
admin.site.register(Occurrence)
admin.site.register(Taxon)
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Identification)
# Register your models here.

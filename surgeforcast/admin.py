from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Message)
admin.site.register(Typhoon)
admin.site.register(SurgeEvent)
admin.site.register(SurgeFrame)
admin.site.register(TriangleElement)
admin.site.register(ElevTimeSeries)
admin.site.register(MaxSurge)
admin.site.register(Towns)
admin.site.register(EarliestSurge)
admin.site.register(AffectedLocations)

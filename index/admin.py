from django.contrib import admin
from .models import BioData, Results, Courses, Registered, Projects

# Register your models here.
admin.site.register(BioData)
admin.site.register(Results)
admin.site.register(Courses)
admin.site.register(Registered)
admin.site.register(Projects)

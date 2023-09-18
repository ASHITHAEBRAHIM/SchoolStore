from django.contrib import admin
from .models import std_form,department,purpose,course
# Register your models here.
admin.site.register(std_form)
admin.site.register(department)
admin.site.register(course)
admin.site.register(purpose)

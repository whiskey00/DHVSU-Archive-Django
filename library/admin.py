from django.contrib import admin

from . models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Document)
admin.site.register(Author)
admin.site.register(Adviser)


from django.contrib import admin
from .models import *


admin.site.register(Category)
prepopulated_fields = {"slug": ("name",)}

admin.site.register(CarForRent)
admin.site.register(FeaturedCarForRent)
admin.site.register(Contact)
admin.site.register(NeedADriver)
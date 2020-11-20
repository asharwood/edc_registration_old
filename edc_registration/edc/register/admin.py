from django.contrib import admin
from .models import User, Condition, Dataset
from .forms import *


from django.contrib.auth.models import User as SiteUser
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
   list_display=('id', 'title', 'firstName', 'lastName', 'emailaddress', 'startdate')
   
admin.site.register(User, UserAdmin)

class ConditionAdmin(admin.ModelAdmin):
   form = ConditionForm
   list_display=('id', 'dataset', 'version', 'comment')
   
admin.site.register(Condition, ConditionAdmin)

class DatasetAdmin(admin.ModelAdmin):
   list_display=('id', 'name')
   
admin.site.register(Dataset, DatasetAdmin)

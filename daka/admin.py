from django.contrib import admin
from daka import models




class MyuserAdmin(admin.ModelAdmin):
    list_display = ('id','name','c_time','uuid')
    search_fields = ('name','uuid')

# Register your models here.
admin.site.register(models.Myuser,MyuserAdmin)
from django.contrib import admin
from .models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_at')
    list_display_links = ('title', 'created_at')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','phone_number')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Contact, ContactAdmin)
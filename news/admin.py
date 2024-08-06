from django.contrib import admin
from news.models import News, Category, ContactUs,Subscriber, SocialMedia
# Register your models here.

admin.site.register (News)
admin.site.register (Category)
admin.site.register (ContactUs)
admin.site.register (Subscriber)
admin.site.register (SocialMedia)
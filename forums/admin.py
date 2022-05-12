from django.contrib import admin

from forums.models import Forum_Posts, Review, Complaint

# Register your models here.
admin.site.register(Forum_Posts)
admin.site.register(Review)
admin.site.register(Complaint)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Customer, Chef, Deliverer

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Chef)
admin.site.register(Deliverer)

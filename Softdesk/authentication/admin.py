from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'age', 'can_be_contacted', 'can_data_be_shared', 'created_time')
    search_fields = ('email', 'username')

from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'user', 'created_at', 'updated_at')
    
    # Fields to search in the admin search bar
    search_fields = ('title', 'content')
    
    # Filters for the list view
    list_filter = ('user', 'created_at')
    
    # Read-only fields
    readonly_fields = ('created_at', 'updated_at')
    
    # Fieldsets for organizing the admin form layout
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'user')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

# Register the Note model with the customized NoteAdmin
admin.site.register(Note, NoteAdmin)

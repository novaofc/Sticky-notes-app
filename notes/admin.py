from django.contrib import admin
from .models imporet note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
  """Register the Note model with the Django admin."""
  list_display = ('title', 'created_at', 'updated_at')
  list_filter = ('created_at', 'updated_at')
  search_fields = ('title', 'content')
  readonly_fields = ('created_at', 'updated_at')

# Register your models here.

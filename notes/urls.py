from django. urls import path
from . import views

app_name = 'notes'  # Namespace for reverse URLs (eg 'notes:list')

urlpatterns = [
    path('', views.list_notes, name='list'),  # GET/ show all notes
    path('create/', views.create_note, name='create'),  # GET/POST create note
    path('<int:pk>/', views.note_detail, name='detail'),  # GET/<id> show one note
    path('<int:pk>/edit/', views.edit_note, name='edit'),  # GET/POST/<id>/edit edit note
    path('<int:pk>/delete', views.delete_note, name='delete'),  # POST/<id>/delete delete note
]

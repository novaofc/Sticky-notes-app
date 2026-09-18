from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Note
from .forms import NoteForm


def list_notes(request):
    """Display all notes."""
    notes = Note.objects.all()
    return render(request, 'notes/list.html', {'notes': notes})


def note_detail(request, pk):
    """Display a single note."""
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/detail.html', {'note': note})


def create_note(request):
    """Create a new note."""
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:list')
    else:
        form = NoteForm()

    return render(request, 'notes/form.html', {'form': form})


def edit_note(request, pk):
    """Edit an existing note."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)  # instance=note updates existing
        if form.is_valid():
            form.save()
            return redirect('notes:detail', pk=note.pk)

    else:
        form = NoteForm(instance=note)  # prefill form with current data

    return render(request, 'notes/form.html', {'form': form, 'note': note})


@require_http_methods(["POST"])
def delete_note(request, pk):
    """Delete a note. POST only to prevent accidental deletion"""
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes:list')
# Create your views here.

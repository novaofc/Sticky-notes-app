from django.test import TestCase
from django.urls import reverse
from .models import Note
from .forms import NoteForm


class NoteModelTest(TestCase):
    """Tests for the Note model."""

    def setUp(self):
        """Create a Note object for testing."""
        Note.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    def test_note_has_title(self):
        """Test that a Note object has the expected title."""
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        """Test that a Note object has the expected content."""
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')

    def test_note_str_method(self):
        """Test that the __str__ method returns the title."""
        note = Note.objects.get(id=1)
        self.assertEqual(str(note), 'Test Note')


class NoteViewTest(TestCase):
    """Tests for Note views."""

    def setUp(self):
        """Create a Note object for testing views."""
        Note.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    def test_note_list_view(self):
        """Test the note list view returns 200 and displays note."""
        response = self.client.get(reverse('notes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        """Test the note detail view displays the correct note."""
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('notes:detail',
                                           args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')


class NoteFormTest(TestCase):
    """Tests for the NoteForm."""

    def test_valid_form(self):
        """Test that a valid form is created correctly."""
        form_data = {
            'title': 'Test Note',
            'content': 'This is a test note.'
        }
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_missing_title(self):
        """Test that form is invalid without a title."""
        form_data = {
            'title': '',
            'content': 'This is a test note.'
        }
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())
# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .models import Note
from .forms import NoteForm


class NoteModelTest(TestCase):
    """Tests for the Note model."""

    def setUp(self):
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_has_title(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')

    def test_note_str_method(self):
        note = Note.objects.get(id=1)
        self.assertEqual(str(note), 'Test Note')


class NoteViewTest(TestCase):
    """Tests for Note views."""

    def setUp(self):
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_list_view(self):
        response = self.client.get(reverse('notes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        note = Note.objects.get(id=1)
        response = self.client.get(
            reverse('notes:detail', args=[str(note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')

    def test_create_note_get(self):
        response = self.client.get(reverse('notes:create'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], NoteForm)

    def test_create_note_post(self):
        response = self.client.post(
            reverse('notes:create'),
            {'title': 'New Note', 'content': 'New content'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)
        self.assertTrue(Note.objects.filter(title='New Note').exists())

    def test_edit_note_get(self):
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('notes:edit', args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_edit_note_post(self):
        note = Note.objects.get(id=1)
        response = self.client.post(
            reverse('notes:edit', args=[str(note.id)]),
            {'title': 'Updated Note', 'content': 'Updated content'},
        )
        self.assertEqual(response.status_code, 302)
        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated Note')

    def test_delete_note(self):
        note = Note.objects.get(id=1)
        response = self.client.post(
            reverse('notes:delete', args=[str(note.id)])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)


class NoteFormTest(TestCase):
    """Tests for the NoteForm."""

    def test_valid_form(self):
        form = NoteForm(data={'title': 'Test Note', 'content':
                              'This is a test note.'})
        self.assertTrue(form.is_valid())

    def test_form_missing_title(self):
        form = NoteForm(data={'title': '', 'content': 'This is a test note.'})
        self.assertFalse(form.is_valid())

from django.test import TestCase

from django.test import Client
from django.urls import reverse

from .models import Todo


class TodoModelTests(TestCase):
    def test_create_and_mark_complete(self):
        t = Todo.objects.create(title="Test", description="Desc")
        self.assertFalse(t.completed)
        t.mark_completed()
        t.refresh_from_db()
        self.assertTrue(t.completed)
        self.assertIsNotNone(t.completed_at)
        t.mark_incomplete()
        t.refresh_from_db()
        self.assertFalse(t.completed)
        self.assertIsNone(t.completed_at)


class TodoViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_get_and_post_create(self):
        resp = self.client.get(reverse("todos:index"))
        self.assertEqual(resp.status_code, 200)
        # create a new todo
        resp = self.client.post(
            reverse("todos:index"), {"title": "Home", "description": "x"}
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Todo.objects.count(), 1)

    def test_toggle_and_delete(self):
        t = Todo.objects.create(title="a")
        # toggle
        resp = self.client.post(reverse("todos:toggle", args=[t.pk]))
        self.assertEqual(resp.status_code, 302)
        t.refresh_from_db()
        self.assertTrue(t.completed)
        # delete
        resp = self.client.post(reverse("todos:delete", args=[t.pk]))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)

    def test_index_renders_and_form_validation(self):
        # Ensure index renders and shows form errors for empty title
        resp = self.client.get(reverse("todos:index"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '<form')

        # Post invalid (empty title) - ModelForm requires title, so it should not redirect
        resp = self.client.post(reverse("todos:index"), {"title": "", "description": "x"})
        # Should return 200 and show form with errors
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'This field is required')

    def test_template_content(self):
        # Create a todo and ensure it appears in the rendered template
        t = Todo.objects.create(title="Template Test", description="Desc")
        resp = self.client.get(reverse("todos:index"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Template Test')

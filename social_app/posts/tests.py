from django.test import TestCase

from .forms import AddPost


class PostTextOnlyTests(TestCase):
    def test_add_post_form_has_no_image_field(self):
        form = AddPost()

        self.assertNotIn("image_url", form.fields)
        self.assertIn("title", form.fields)
        self.assertIn("content", form.fields)

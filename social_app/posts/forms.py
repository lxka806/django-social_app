from django import forms


class AddPost(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"placeholder": "Give your post a title"}
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Share something with your people...",
                "rows": 6
            }
        )
    )

    post_image = forms.ImageField(required=False, widget=forms.FileInput())

    def clean_title(self):
        post_title = self.cleaned_data["title"]

        if not post_title.strip():
            raise forms.ValidationError("Title is required")

        return post_title

    def clean_content(self):
        post_content = self.cleaned_data["content"]

        if not post_content.strip():
            raise forms.ValidationError("Content is required")

        return post_content


class AddComment(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write a comment...",
                "rows": 3
            }
        )
    )
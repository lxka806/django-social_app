from django import forms 

class AddPost(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"placeholder": "Give your post a title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Share something with your people...", "rows": 6}))
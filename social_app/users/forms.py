from django import forms

class registerForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']

        for char in username:
            if char.isdigit() or char in "@#$":
                raise forms.ValidationError(
                    "Username must not contain numbers or @, #, $ symbols."
                )

        return username

    def clean_email(self):
        email = self.cleaned_data["email"]

        if not email.endswith("@gmail.com"):
            raise forms.ValidationError(
                "Email must end with @gmail.com."
            )

        return email

    def clean_password(self):
        password = self.cleaned_data["password"]

        if len(password) < 8:
            raise forms.ValidationError(
                "Password must contain at least 8 characters."
            )

        has_number = False

        for char in password:
            if char.isdigit():
                has_number = True

        if not has_number:
            raise forms.ValidationError(
                "Password must contain at least one number."
            )

        return password

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


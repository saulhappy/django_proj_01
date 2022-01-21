from django.contrib.auth import get_user_model
from django.forms import forms, widgets

User = get_user_model()

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    password2 = forms.CharField(
        label = "Confirm Password",
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password"
            }
        )
    )

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password"
            }
        )
    )

    def validate_username(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)

        if not qs.exists():
            raise forms.ValidationError("Email not found")
        
        return email

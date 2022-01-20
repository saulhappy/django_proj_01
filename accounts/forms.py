from django.contrib.auth import get_user_model
from django.forms import forms, widgets

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.Charfield()
    pasword = forms.Charfield(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password"
            }
        )
    )

    def validate_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)

        if not qs.exists():
            raise forms.ValidationError("Invalid user")
        
        return username

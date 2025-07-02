from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'class': 'input'
        })
        self.fields["last_name"].widget.attrs.update({
            'class': 'input'
        })
        self.fields["username"].widget.attrs.update({
            'class': 'input'
        })
        self.fields["password1"].widget.attrs.update({
            'class': 'input'
        })
        self.fields["password2"].widget.attrs.update({
            'class': 'input'
        })


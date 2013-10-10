from django import forms
from polls.models import Poll
from django.contrib.auth.models import User


class PollAnswerForm(forms.Form):
    poll = forms.ModelChoiceField(queryset=Poll.objects.all())
    answer = forms.CharField()

class PollForm(forms.ModelForm):

    class Meta(object):
        model = Poll

# class
#     choices = forms.ModelChoiceField(widget)

class UserForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "password":forms.PasswordInput,
            "confirm_password":forms.PasswordInput
        }

class SignupForm(UserForm):
    confirm_password = forms.CharField()
    widget = forms.PasswordInput

    def clean(self):
        password = self.cleaned_data.get("password")
        password_conf = self.cleaned_data.get("confirm_password")
        if password is not None and password != password_conf:
            raise forms.ValidationError(
                "Password confirmation does not match password"
            )
        return self.cleaned_data

# class LoginForm(UserForm):
#     def clean(self):
#         return self.cleaned_data

class Authenticate(forms.Form):
    model = User
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField()
    # widget = forms.PasswordInput
    #
    # def clean(self):
    #     password = self.cleaned_data.get("password")
    #     password_conf = self.cleaned_data.get("confirm_password")
    #     if password is not None and password != password_conf:
    #         raise forms.ValidationError(
    #             "Password confirmation does not match password"
    #         )
    #     return self.cleaned_data
    # class Meta(object):
    #     model = User
    #     fields = ["username", "email", "password"]
    #     widgets = {
    #         "password":forms.PasswordInput,
    #         "confirm_password":forms.PasswordInput
    #     }
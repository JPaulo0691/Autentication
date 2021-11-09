from django import forms

# At this place we create our class form that provides username and password. This form will be used for user authentication with database. Notice that we use widget Password Input that will render the password HTML element.

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

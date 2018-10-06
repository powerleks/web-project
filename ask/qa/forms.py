from django import forms
from django.contrib.auth.models import User
from qa.models import Answer, Question

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    # def clean(self):
    #     # random_user = User.objects.first()
    #     self.cleaned_data['author'] = self._user
    #     return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    choices = (
        ('Question', 'Question'),
    )
    question = forms.ChoiceField(choices=choices)

    # def clean(self):
    #     # random_user = User.objects.first()
    #     self.cleaned_data['author'] = self._user
    #     return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
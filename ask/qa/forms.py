from django import forms
from django.contrib.auth.models import User
from qa.models import Answer, Question

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    # def clean(self):
    #     random_user = User.objects.first()
    #     self.cleaned_data['author'] = random_user

    def save(self):
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
    #     random_user = User.objects.first()
    #     self.cleaned_data['author'] = random_user

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
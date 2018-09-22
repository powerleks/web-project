from django import forms
from qa.models import Answer, Question

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    # def clean(self):
    #     if is_spam(self.clean_data):
    #         raise forms.ValidationError(
    #         'Сообщение похоже на спам',
    #         code='spam'
    #     )

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    # title = forms.CharField(max_length=100)
    # question = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Answer
        fields = ['text', 'question']

    # def clean(self):
    #     if is_spam(self.clean_data):
    #         raise forms.ValidationError(
    #         'Сообщение похоже на спам',
    #         code='spam'
    #     )

    # def save(self):
    #     question = Question(**self.cleaned_data)
    #     question.save()
    #     return question
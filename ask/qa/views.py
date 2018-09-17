from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from qa.models import Question
from django.core.urlresolvers import reverse

def new_questions(request):
    questions = Question.objects.new()
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = reverse('ask', )
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/index.html', {
        'questions': page,
    })

def popular_questions(request):
    questions = Question.objects.popular()
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/index.html', {
        'questions': page,
    })


def question_page(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, 'qa/question.html', {
        'question': question,
    })

def test(request, *args, **kwargs):
    return HttpResponse('OK')

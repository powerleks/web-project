from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from qa.models import Question
from qa.forms import AnswerForm, AskForm

def new_questions(request):
    questions = Question.objects.new()
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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'qa/question.html', {
        'question': question,
        'form': form,
    })

def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/question_add.html', {
        'form': form,
    })

def test(request, *args, **kwargs):
    return HttpResponse('OK')
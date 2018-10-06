from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from qa.models import Question
from qa.forms import AnswerForm, AskForm, SignupForm, LoginForm

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
            form.cleaned_data['question'] = question
            form._user = request.user
            answer = form.save()
            url = answer.question.get_url()
            return HttpResponseRedirect(url)
        else:
            print('form is invalid!!!!!!!!!!!!!!!!')
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
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/question_add.html', {
        'form': form,
    })

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {
        'form': form,
    })

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            form = LoginForm(request.POST)
    else:
        form = LoginForm()
    return render(request, 'qa/signup.html', {
        'form': form,
    })

def test(request, *args, **kwargs):
    return HttpResponse('OK')
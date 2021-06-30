from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Category, Question, Choice

def index(request):
    category = Category.objects.all()
    return render(request, 'myapp/index.html', {'category': category})



def test(request):
    categ1 = Category.objects.get(pk=Category)
    question = Question.objects.filter(category=categ1)
    return render(request, 'myapp/test.html', {'question': question})
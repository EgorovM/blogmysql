from django.shortcuts import render, redirect

from .models import *
from .forms import  *

def index(request):

    return render(request, 'main/index.html', locals())


def article(request, id):
    article = Article.objects.get(id=id)

    return render(request, 'main/article.html', locals())


def article_list(request):
    article_list = Article.objects.filter()

    return render(request, 'main/article_list.html', locals())


def edit_article(request, id):
    if not request.user.is_staff:
        return render(request, 'bad/access_denied.html', locals())

    if 'msg' in request.GET: msg = request.GET.get('msg')

    article = Article.objects.get(id=id)
    post_form = PostEditForm(initial={'description': article.description})

    if request.method == 'POST':
        if 'save_btn' in request.POST:
            for name in request.POST:
                if hasattr(article, name):
                    val = request.POST[name]
                    if name == 'city':
                        article.city = City.objects.get(id=val)
                    elif name == 'category':
                        article.category = Category.objects.get(id=val)
                    elif name == 'source':
                        article.source = Source.objects.get(id=val)
                    elif name == 'grade':
                        article.grade = Grade.objects.get(id=val)
                    elif name == 'participants':
                        article.participants.clear()
                        for id in request.POST.getlist(name):
                            article.participants.add(Participant.objects.get(id=int(id)))
                    else:
                        print(name, request.POST.get(name))
                        setattr(article, name, val)
                        print(name, getattr(article, name))

            article.save()
            msg = 'Успешно сохранено!'

    return render(request, 'main/edit_article.html', locals())


def add_article(request):
    if not request.user.is_staff:
        return render(request, 'bad/access_denied.html', locals())

    article = Article.objects.create()

    return redirect(f'/edit_article/{article.id}?msg=Успешно создано. Можно приступать к редактированию')

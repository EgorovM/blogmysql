from django.shortcuts import render, redirect

from .models import *
from .forms import  *

def index(request):

    return render(request, 'main/index.html', locals())


def article(request, id):
    article = Article.objects.get(id=id)
    title = f'{article.category} {article.name}'
    return render(request, 'main/article.html', locals())


def article_list(request):
    if 'view_all' in request.GET:
        article_list = Article.objects.all()
    else:
        article_list = Article.objects.filter(status='PUB')

    return render(request, 'main/article_list.html', locals())


def edit_article(request, id):
    if not request.user.is_staff:
        return render(request, 'bad/access_denied.html', locals())

    if 'msg' in request.GET: msg = request.GET.get('msg')

    article = Article.objects.get(id=id)
    post_form = PostEditForm(initial={
        'description': article.description,
        'requirements': article.requirements,
        'contacts': article.contacts
    })

    if request.method == 'POST':
        if 'save_btn' in request.POST:
            article.upon_request = True if 'upon_request' in request.POST else False
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
                    elif name == 'scopes':
                        article.scopes.clear()
                        for id in request.POST.getlist(name):
                            article.scopes.add(Scope.objects.get(id=int(id)))
                    elif name == 'project_directions':
                        article.project_directions.clear()
                        for id in request.POST.getlist(name):
                            article.project_directions.add(ProjectDirection.objects.get(id=int(id)))
                    elif name == 'purpose':
                        article.purpose.clear()
                        for id in request.POST.getlist(name):
                            article.purpose.add(Purpose.objects.get(id=int(id)))
                    elif name == 'upon_request':
                        pass
                    else:
                        if name == 'name' and val != '':
                            article.status = 'PUB'
                        setattr(article, name, val)

            article.save()
            msg = 'Успешно сохранено!'

        elif 'add-scope' in request.POST:
            scope_name = request.POST['scope_name']
            scope = Scope.objects.create(name=scope_name)
            msg = f'Cфера {scope.name} создана'
        elif 'add-purpose' in request.POST:
            purpose_name = request.POST['purpose_name']
            purpose = Purpose.objects.create(name=purpose_name)
            msg = f'Цель финансирования {purpose.name} создана'
        elif 'add-direction' in request.POST:
            direction_name = request.POST['direction_name']
            direction = ProjectDirection.objects.create(name=direction_name)
            msg = f'Направление проектов {direction.name} создана'

    return render(request, 'main/edit_article.html', locals())


def add_article(request):
    if not request.user.is_staff:
        return render(request, 'bad/access_denied.html', locals())

    article = Article.objects.create()

    return redirect(f'/edit_article/{article.id}?msg=Можно приступать к редактированию')

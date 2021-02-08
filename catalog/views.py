from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import ListView,DetailView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.db.models import Q

from .models import *
from .form import *

class HomePage(ListView):
    model = Items
    template_name = 'catalog/index.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['category_list'] = category.objects.all()
        context['title'] = 'eShop'
        context['check'] = [i for i in range(0,101,3)][1::]
        return context

def get_category(request, category_uniCat):
     Category = category.objects.get(uniCat=category_uniCat)
     items = Items.objects.filter(category=Category.pk)
     print(items)
     category_list = category.objects.all()
     contex = {'items':items,
               'category': Category,
               'title':'eShop: ' + Category.category,
               'category_list':category_list}
     return render(request, 'catalog/category.html', contex)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, 'Отлично')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка')
    else:

        form = UserRegisterForm()
    return render(request,'catalog/register.html',{'form': form,})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            print(user)
            return redirect('home')
        else:
            messages.error(request, 'Неверный логин\пароль' )
    else:
        form = UserLoginForm()
    return render(request,'catalog/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('home')

class PlaceListView(ListView):
    model = Items
    template_name = 'catalog/404.html'

    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super(PlaceListView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            print(queryset.filter(Q(shortName__icontains=q)))
            return queryset.filter(Q(shortName__icontains=q))
        print('not: ',queryset)
        return redirect('home')

class TestPage(ListView):
    template_name = 'catalog/404.html'
    context_object_name = 'items'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TestPage, self).get_context_data(**kwargs)
        context['listPag'] = [i for i in range(0,101,4)][1::]
        return context

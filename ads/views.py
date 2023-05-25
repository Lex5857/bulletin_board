from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Ads, Responses, Author
from .filters import AdsFilter
from .forms import AdsForm, ResponsesForm
from .forms import UserForm, AuthorForm


class AdsList(ListView):
    model = Ads
    ordering = 'heading'
    template_name = 'all_ads.html'
    context_object_name = 'all_ads'
    paginate_by = 2

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = AdsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        return context


class ResponsesList(ListView):
    model = Responses
    ordering = 'time_in'
    template_name = 'all_responses.html'
    context_object_name = 'all_responses'
    paginate_by = 2


class AdsDetail(DetailView):
    model = Ads
    template_name = 'ads.html'
    context_object_name = 'ads'


class ResponsesDetail(DetailView):
    model = Responses
    template_name = 'responses.html'
    context_object_name = 'responses'


class AdsUpdate(LoginRequiredMixin, UpdateView):
    form_class = AdsForm
    model = Ads
    template_name = 'ads_edit.html'
    success_url = reverse_lazy('ads_detail')


class ResponsesUpdate(LoginRequiredMixin, UpdateView):
    form_class = ResponsesForm
    model = Responses
    template_name = 'responses_edit.html'
    success_url = reverse_lazy('responses_detail')


class AdsDelete(LoginRequiredMixin, DeleteView):
    model = Ads
    template_name = 'ads_delete.html'
    success_url = reverse_lazy('ads_list')


class ResponsesDelete(LoginRequiredMixin, DeleteView):
    model = Responses
    template_name = 'responses_delete.html'
    success_url = reverse_lazy('responses_list')


class AdsCreate(LoginRequiredMixin, CreateView):
    form_class = AdsForm
    model = Ads
    template_name = 'ads_edit.html'
    success_url = reverse_lazy('ads_list')


class ResponsesCreate(LoginRequiredMixin, CreateView):
    form_class = ResponsesForm
    model = Responses
    template_name = 'responses_edit.html'
    success_url = reverse_lazy('responses_list')


class UserCreate(CreateView):
    form_class = UserForm
    model = User
    template_name = 'user_edit.html'
    success_url = reverse_lazy('author_create')


class AuthorCreate(CreateView):
    form_class = AuthorForm
    model = Author
    template_name = 'author_edit.html'
    success_url = reverse_lazy('ads_list')

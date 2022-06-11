from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import LoginForm


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'reconciliation_app/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

    def get_success_url(self):
        return reverse_lazy('rc_app:reconciliation_page')


@login_required(login_url='rc_app:login_page')
def reconciliation_page(request):
    return HttpResponse('Сверка')

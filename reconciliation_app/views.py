import datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import LoginForm
from .models import ProductCategory, Product, ReconciliationDate


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'reconciliation_app/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

    def get_success_url(self):
        return reverse_lazy('rc_app:reconciliation_page')


@login_required(login_url='rc_app:login_view')
def logout_view(request):
    logout(request)
    return redirect('rc_app:login_view')


@login_required(login_url='rc_app:login_view')
def reconciliation_page(request):
    categories = ProductCategory.objects.all()
    if request.method == 'POST':
        cleaned_data = request.POST.copy()
        del cleaned_data['csrfmiddlewaretoken']
        for p in cleaned_data:
            if cleaned_data[p]:
                dates = [d.date for d in ReconciliationDate.objects.filter(product=int(p))]
                d = datetime.datetime.strptime(cleaned_data[p], "%Y-%m-%d").date()
                if d not in dates:
                    ReconciliationDate.objects.create(
                        date=datetime.datetime.strptime(cleaned_data[p], "%Y-%m-%d"),
                        product=Product.objects.get(pk=int(p))
                        )
    # date = ReconciliationDate.objects.all()
    # print(date)

    context = {'title': 'Сверка', 'categories': categories}
    return render(request, 'reconciliation_app/reconciliation_page.html', context)

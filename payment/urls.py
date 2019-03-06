from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

app_name = 'payment'

urlpatterns = [
    re_path(r'^$', login_required(views.AddBankAccount.as_view()), name='show_all'),
    path('add/', login_required(views.AddBankAccount.as_view()), name='add_new'),
]
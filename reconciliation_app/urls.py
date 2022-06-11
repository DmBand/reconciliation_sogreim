from django.urls import path
from .views import *

app_name = 'rc_app'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('', reconciliation_page, name='reconciliation_page'),
]

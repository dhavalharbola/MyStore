from django.urls import path
from .views import sign_up,log_in,log_out

urlpatterns = [
    path('accounts/sign_up',sign_up,name='sign_up'),
    path('accounts/log_in',log_in,name='log_in'),
    path('accounts/log_out',log_out,name='log_out'),

]
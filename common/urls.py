from common.views import index as ind, RegisterView, CreateUserProfile
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from allauth.account.views import login, logout

app_name = 'common'
urlpatterns = [
  path('common/', ind, name='index_common'),
  path('login/', login, name='login'),
  path('logout/', logout, name='logout'),
  path('register/', RegisterView.as_view(
        template_name='register.html',
		success_url=reverse_lazy('common:profile-create')
    ), name='register'),
  path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
]

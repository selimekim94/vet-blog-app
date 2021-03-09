from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomSignUpView, CustomEditView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', CustomSignUpView.as_view(), name='signup'),
    path('edit_profile/', CustomEditView.as_view(), name='profile_edit'),
]

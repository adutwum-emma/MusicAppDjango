from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('<int:user_id>', views.profile, name="profile"),
    path('<int:user_id>/editProfile/', views.editProfile, name="editProfile"),
    path('delete', views.delete, name="delete"),
    path('<int:user_id>/changePass/', views.changePass, name="changePass"),
]
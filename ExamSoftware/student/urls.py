from django.urls import path
from .views import *

app_name = "student"
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgot_password/', ForgotPasswordView.as_view(),
         name='forgot_password'),
    path('join/', JoinTestView.as_view(), name='join'),
    path('join/<int:id>', StartTestView.as_view(), name='start'),
    path('calculator/', CalculatorPoint, name='calculator'),
    path('result/', ResultView.as_view(), name='result'),
    path('result/detail/<int:id>/<int:key>',
         DetailResultView, name='result_detail'),
    path('notification/', NotificationView.as_view(), name='notification'),
    path('notification/<str:slug>',
         NotificationDetailView, name='notif_detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('avatar/', UpdateAvatar, name='avatar'),
    path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('change_pass/', ChangePassView.as_view(), name='change_pass'),
]

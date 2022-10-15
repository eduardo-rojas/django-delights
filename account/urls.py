from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login / log out urls
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # # Change password urls
    # path('password-change/', 
    #     auth_views.PasswordChangeView.as_view(),
    #     name='password_change'),
    # path('password-change/done/',
    #     auth_views.PasswordChangeDoneView.as_view(),
    #     name='password_change_done'),

    # # reset password urls
    # path('password-reset/',
    #     auth_views.PasswordResetView.as_view(),
    #     name="password_reset"),
    # path('password-reset/done',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'),
    # path('password-reset/complete/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'),

#     admin/
#   account/ login/ [name='login']
#   account/ logout/ [name='logout']
#   account/ password_change/ [name='password_change']
#   account/ password_change/done/ [name='password_change_done']
#   account/ password_reset/ [name='password_reset']
# account/ password_reset/done/ [name='password_reset_done']
# account/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# account/ reset/done/ [name='password_reset_complete']
# account/ [name='dashboard']
# account/ register/ [name='register']
# ^media/(?P<path>.*)$
    
    # Dashboard
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register')
    
]
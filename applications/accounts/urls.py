
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from applications.accounts.views import RegisterUserView, user_activate, ChangeUserInfoView, \
    FavoriteRentObjectListView, FavoriteAdd, FavoriteGet, FavoriteRemove, HistoryRentObjectListView, \
    RentStatusGet, CustomPasswordChangeView, CustomPasswordResetView, CustomPasswordResetConfirmView
from django.contrib.auth.views import LoginView

urlpatterns = [

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('accounts/reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/profile/', ChangeUserInfoView.as_view(), name='profile'),
    # path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', ChangeUserInfoView.as_view(), name='profile'),
    path('accounts/favorite_rent_object_list/', FavoriteRentObjectListView.as_view(), name='favorite_rent_object_list'),
    path('accounts/history/', HistoryRentObjectListView.as_view(), name='history'),

    path('favorite_add/<int:id>/', FavoriteAdd.as_view(), name='favorite_add'),
    path('favorite_get/<int:id>/', FavoriteGet.as_view(), name='favorite_get'),
    path('favorite_remove/<int:id>/', FavoriteRemove.as_view(), name='favorite_remove'),

    path('rent_status_get/<int:id>/', RentStatusGet.as_view(), name='rent_status_get'),

]

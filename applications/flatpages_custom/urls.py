from applications.flatpages_custom import views
from django.urls import path

urlpatterns = [
    path('<path:url>', views.flatpage, name='flatpage_custom)'),
]

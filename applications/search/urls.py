from django.urls import path

from applications.objects.views import ObjectListView
# from applications.search.views import NoticeVersionPublicListView, SchedulePublicListView, \
#     SchedulePPGPublicListView, NoticeVersionPublicDetailView

# app_name = 'search'

urlpatterns = [
    # path('purchases-all/', NoticeVersionPublicListView.as_view(), name='purchases-all'),
    # path('purchase-public/purchases/notice/<int:pk>/', NoticeVersionPublicDetailView.as_view(), name='purchase-public'),
    # path('planning-all/', SchedulePublicListView.as_view(), name='planning-all'),
    # path('planning-ppg-all/<int:pk>/', SchedulePPGPublicListView.as_view(), name='planning-ppg-all'),
    # path('search/', ObjectListView.as_view(), name='search'),
]

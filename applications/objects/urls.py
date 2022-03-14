from django.urls import path

from . import views

urlpatterns = [
    path('object/search_result/', views.SearchResultRentObjectListView.as_view(), name='search_result'),
    path('object/filter/', views.FilterObjectListView.as_view(), name='filter_rent_object'),
    # path('object/search_result/<str:property_type>', views.SearchResultObjectListView.as_view(), name='search_result'),

    path('object/<str:type_of_deal>/', views.RentObjectListView.as_view(), name='objects'),
    path('object/<str:type_of_deal>/search_by_name/', views.FilterByNameObjectListView.as_view(), name='search_by_name'),
    path('object/detail/<int:pk>/', views.RentObjectDetailView.as_view(), name='object_detail'),
    path('object/detail/<int:pk>/review/', views.AddReview.as_view(), name='post'),
    path('object/detail/<int:pk>/refresh/', views.ReviewRender.as_view(), name='refresh'),
    path('object/detail/<int:pk>/reserved/', views.AddReserv.as_view(), name='reserved'),
    path('object/detail/<int:pk>/checkreserv/', views.RentObjectDetailView.as_view(), name='reserved'),
]

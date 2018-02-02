from django.conf.urls import include
from django.urls import path
from api import views

urlpatterns = [
    path('user/<int:pk>/', views.UserProfileView.as_view(), ),
    path('user/rides/', views.RideListView.as_view(), name='user-rides'),
    path('user/rides/<int:pk>/', views.RideDetailView.as_view(), name='user-rides'),
    path('driver/<int:pk>/', views.DriverProfileView.as_view(), ),
    path('driver/', views.RideListView.as_view(), name='user-rides'),
    path('offer/', views.OfferListView.as_view(), ),
    path('offer/<int:pk>/', views.OfferDetailView.as_view(), ),
    # path(r'^user/cars/$', views.CarListView.as_view(), name='user-cars'),
]

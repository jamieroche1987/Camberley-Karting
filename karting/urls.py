from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.BookingsListView.as_view(),
         name='booking-home'),
    path('booking/create', views.CreateBooking.as_view(),
         name='createbooking'),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(),
         name='booking-detail'),
    path('booking/<int:pk>/delete/', views.BookingDeleteView.as_view(),
         name='booking-delete'),
    path('booking/select_package/', views.SelectPackageView.as_view(),
         name='select-package')
    path('booking/booking-create/', views.BookingWizardView.as_view(
        [views.SelectPackageform, views.SelectDateForm, views.SelectTimeForm]), name='booking-wizard'),
]
]

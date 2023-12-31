from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.BookingsListView.as_view(),
         name='booking-home'),
    path('booking/booking-past', views.PastBookingsView.as_view(),
         name='booking-past'),
    path('booking-create', views.CreateBookingView.as_view(),
         name='booking-create'),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(),
         name='booking-detail'),
    path('booking/<int:pk>/update/', views.UpdateBookingView.as_view(),
         name='booking-update'),
    path('booking/<int:pk>/confirm/', views.ConfirmBookingView.as_view(),
         name='confirm-booking'),
    path('booking/<int:pk>/delete/', views.BookingDeleteView.as_view(),
         name='confirm-delete'),
]

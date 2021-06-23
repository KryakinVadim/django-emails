from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmailListView.as_view(), name="email_list"),
    path('add/', views.EmailCreateView.as_view(), name="email_create"),
    path('<int:pk>/detail/', views.EmailDetailView.as_view(), name="email_detail"),
    path('<int:pk>/update/', views.EmailUpdateView.as_view(), name="email_update"),
    path('<int:pk>/delete/', views.EmailDeleteView.as_view(), name="email_delete")
]

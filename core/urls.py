from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IPOListView.as_view(), name='ipo_list'),
    path('ipo/<int:pk>/', views.IPODetailView.as_view(), name='ipo_detail'),
] 
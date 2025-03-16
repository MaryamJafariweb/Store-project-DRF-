from django.urls import path
from . import views


app_name = 'ordering'
urlpatterns = [
    path('cart/', views.OrderingView.as_view(), name='ordering'),
    path('add/<int:product_id>/', views.AddCartView.as_view(), name='add'),
    path('detail/<int:order_id>/', views.OrderDetailView.as_view(), name='detail'),
]
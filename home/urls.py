from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    # path('', views.FeaturedView.as_view(), name='featured'),
    # path('', views.OfferView.as_view(), name='offer'),
    # path('', views.OfferView.as_view(), name='offer'),
]
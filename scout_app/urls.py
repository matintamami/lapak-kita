from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    # path('/product', views.product_list)
    # path('', include('scout_app.urls'))
]

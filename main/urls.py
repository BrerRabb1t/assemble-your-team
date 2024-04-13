from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path('product/<slug:product_slug>/', views.product, name='product'),

]
from django .urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name = 'product_list'),
    path('details/<int:pk>', views.product_details, name = 'product_details'),
    path('delete/<int:pk>', views.delete, name = 'delete'),
    path('edit/<pk>', views.edit, name ='edit')
]
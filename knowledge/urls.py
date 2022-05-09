from django.urls import path
from . import views



urlpatterns = [
    # path('list/', views.EquipmentListView.as_view(), name='equipment-list'),
    path('manufacturer-create/', views.ManufacturerCreateView.as_view(), name='manufacturer-create'),
    path('manufacturer-list/', views.ManufacturerListView.as_view(), name='manufacturer-list'),
    path('manufacturer-delete/<int:pk>/', views.ManufacturerDeleteView.as_view(), name='manufacturer-delete'),
    path('manufacturer-update/<int:pk>/', views.ManufacturerUpdateView.as_view(), name='manufacturer-update'),
    

    
    

    
]

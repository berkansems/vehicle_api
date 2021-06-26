from django.urls import path
from myApp.views import *

urlpatterns = [
    path('vehicles/', vehicles_view ),
    path('vehicle_operations/<str:pk>/', vehicle_operations ),

    path('vehicle_models/', vehicle_models_view ),
    path('vehicle_model_operations/<str:pk>/', vehicle_model_operations )
]

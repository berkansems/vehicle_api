from django.urls import path
from myApp.views import *

urlpatterns = [
    path('vehicles/', vehicles ),
    path('vehicle_post/', vehicle_post ),
    path('vehicle_operations/<str:pk>/', vehicle_operations ),

    path('vehicle_models/', vehicle_models ),
    path('vehicle_model_post/', vehicle_model_post ),
    path('vehicle_model_operations/<str:pk>/', vehicle_model_operations )

]

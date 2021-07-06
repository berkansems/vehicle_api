from django.urls import path
from rest_framework.routers import DefaultRouter
from myApp.views import *

router = DefaultRouter()
router.register('models',ModelsViewSet)
urlpatterns = [
    path('vehicles/', vehicles_view ),
    path('vehicle_operations/<str:pk>/', vehicle_operations ),
    path('vehicles_search', vehicles_search ),

    # path('vehicle_models/', vehicle_models_view ),
    # path('vehicle_model_operations/<str:pk>/', vehicle_model_operations)
]

urlpatterns += router.urls

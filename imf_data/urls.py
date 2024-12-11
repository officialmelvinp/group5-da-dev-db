from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'annual-data', views.AnnualDataViewSet)
router.register(r'quarterly-data', views.QuarterlyDataViewSet)

app_name = 'imf_data'

urlpatterns = [
    path('', include(router.urls)),
    path('country-list/', views.country_list, name='country_list'),  # Keep your existing URL pattern
]
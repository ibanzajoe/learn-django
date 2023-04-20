from django.urls import path
from .views import dashboard

app_name = 'reactadmin'
urlpatterns = [
    path('', dashboard),
]
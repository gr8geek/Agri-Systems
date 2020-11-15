from django.urls import path
from .views import predictions
urlpatterns = [
    path('upload/',predictions),

]

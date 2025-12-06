# listings/urls.py

from django.urls import path
from rest_framework import routers # You can use routers for ViewSets
from . import views

urlpatterns = [
    # Example API endpoint (you'll replace this with your actual views)
    # path('hello/', views.hello_world, name='hello_world'),
]

# Example for Django REST Framework ViewSets (if you use them)
# router = routers.DefaultRouter()
# router.register(r'travels', views.TravelViewSet) # Assuming you have a TravelViewSet
# urlpatterns += router.urls



# listings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.HelloWorldView.as_view(), name='hello_world'),
]
from django.urls import path
from policy import views

urlpatterns = [
    path('policy/', views.policy_list),
    path('policy/<int:pk>/', views.policy_detail),
]

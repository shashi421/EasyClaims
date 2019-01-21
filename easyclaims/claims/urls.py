from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('claims/', views.ClaimViewList.as_view()),
    path('claims/<int:pk>/', views.ClaimViewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClaimViewList,ClaimViewDetail

urlpatterns = [
    path('claims/', ClaimViewList.as_view()),
    path('claims/<int:pk>/', ClaimViewDetail.as_view()),
    path('claims/<int:claimNo>/',ClaimStatusDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


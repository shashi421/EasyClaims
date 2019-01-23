from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from claims.views import ClaimViewList,ClaimViewDetail,ClaimStatusDetail,DialogFLowClaimHelper

urlpatterns = [
    path('claims/', ClaimViewList.as_view()),
    path('claims/<int:pk>/', ClaimViewDetail.as_view()),
    path('claimstatus/', ClaimStatusDetail.as_view()),
    path('claimhelper/', DialogFLowClaimHelper.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)


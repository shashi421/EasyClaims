from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from claims.views import ClaimViewList,ClaimViewDetail,ClaimStatusDetail
from . import views

urlpatterns = [
    path('claims/', ClaimViewList.as_view()),
    path('claims/<int:pk>/', ClaimViewDetail.as_view()),
    path('claimstatus/<int:pk>/',ClaimStatusDetail.as_view()),
    path('claimhelper/', views.dialogFLowClaimHelper)
]

urlpatterns = format_suffix_patterns(urlpatterns)


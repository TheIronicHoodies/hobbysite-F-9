from django.urls import path
from .views import CommissionsDetail, CommissionsList

urlpatterns = [
    path('commissions/list', CommissionsList.as_view(), name='commissions-list'),
    path('commissions/detail/<int:pk>', CommissionsDetail.as_view(), name='commissions-detail')
]

app_name = 'commissions'
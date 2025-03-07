from django.urls import path
from .views import CommissionsDetail, CommissionsList

urlpatterns = [
    path('list', CommissionsList.as_view(), name='commissions-list'),
    path('detail/<int:pk>', CommissionsDetail.as_view(), name='commissions-detail')
]

app_name = 'commissions'
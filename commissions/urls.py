from django.urls import path
from .views import *

urlpatterns = [
    path('list', CommissionsList.as_view(), name='commissions-list'),
    path('detail/<int:pk>', CommissionsDetail.as_view(), name='commissions-detail'),
    path('add', CreateCommission.as_view(), name='commissions-add'),
    path('<int:pk>/edit', UpdateCommission.as_view(), name='commissions-edit'),
    path('job/<int:pk>', JobView.as_view(), name='job-detail'),
    path('job/<int:pk>/update', UpdateJob.as_view(), name='job-update'),
]

app_name = 'commissions'
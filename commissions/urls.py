from django.urls import path
from .views import *

urlpatterns = [
    path('list', CommissionsList.as_view(), name='commissions-list'),
    path('detail/<int:pk>', CommissionsDetail.as_view(), name='commissions-detail'),
    path('add', CommissionsCreate.as_view(), name='commissions-add'),
    path('<int:pk>/edit', CommissionsUpdate.as_view(), name='commissions-edit')
]

app_name = 'commissions'